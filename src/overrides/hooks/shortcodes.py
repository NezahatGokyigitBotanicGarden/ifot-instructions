# Copyright (c) 2016-2024 Martin Donath <martin.donath@squidfunk.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from __future__ import annotations

import posixpath
import re

from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page
from re import Match

# -----------------------------------------------------------------------------
# Hooks
# -----------------------------------------------------------------------------

# Handle version shortcode with insiders check
def _handle_version(args: str, page: Page, files: Files):
    if args.startswith("insiders-"):
        return _badge_for_version_insiders(args, page, files)
    return _badge_for_version(args, page, files)

# Handle default shortcode with special cases
def _handle_default(args: str, page: Page, files: Files):
    if args == "none":
        return _badge_for_default_none(page, files)
    if args == "computed":
        return _badge_for_default_computed(page, files)
    return _badge_for_default(args, page, files)

# Replace callback for shortcode processing
def _replace_shortcode(match: Match, page: Page, files: Files):
    ty_pe, args = match.groups()
    args = args.strip()
    
    # Dispatch table for shortcode handlers
    handlers = {
        "version": lambda: _handle_version(args, page, files),
        "sponsors": lambda: _badge_for_sponsors(page, files),
        "flag": lambda: flag(args, page, files),
        "option": lambda: option(args),
        "setting": lambda: setting(args),
        "feature": lambda: _badge_for_feature(args, page, files),
        "plugin": lambda: _badge_for_plugin(args, page, files),
        "extension": lambda: _badge_for_extension(args, page, files),
        "utility": lambda: _badge_for_utility(args, page, files),
        "example": lambda: _badge_for_example(args),
        "default": lambda: _handle_default(args, page, files),
    }
    
    handler = handlers.get(ty_pe)
    if handler:
        return handler()
    
    raise RuntimeError(f"Unknown shortcode: {ty_pe}")

# @todo
def on_page_markdown(
    markdown: str, *, page: Page, files: Files
):
    # Find and replace all external asset URLs in current page
    return re.sub(
        r"<!-- md:(\w+)((?:(?!-->).)*?) -->",
        lambda match: _replace_shortcode(match, page, files),
        markdown,
        flags = re.I | re.M
    )

# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------

# Create a flag of a specific type
def flag(args: str, page: Page, files: Files):
    ty_pe, *_ = args.split(" ", 1)
    if   ty_pe == "experimental":  return _badge_for_experimental(page, files)
    elif ty_pe == "required":      return _badge_for_required(page, files)
    elif ty_pe == "customization": return _badge_for_customization(page, files)
    elif ty_pe == "metadata":      return _badge_for_metadata(page, files)
    elif ty_pe == "multiple":      return _badge_for_multiple(page, files)
    raise RuntimeError(f"Unknown type: {ty_pe}")

# Create a linkable option
def option(ty_pe: str):
    _, *_, name = re.split(r"[.:]", ty_pe)
    return f"[`{name}`](#+{ty_pe}){{ #+{ty_pe} }}\n\n"

# Create a linkable setting - @todo append them to the bottom of the page
def setting(ty_pe: str):
    _, *_, name = re.split(r"[.*]", ty_pe)
    return f"`{name}` {{ #{ty_pe} }}\n\n[{ty_pe}]: #{ty_pe}\n\n"

# -----------------------------------------------------------------------------

# Resolve path of file relative to given page - the posixpath always includes
# one additional level of `..` which we need to remove
def _resolve_path(path: str, page: Page, files: Files):
    path, anchor, *_ = f"{path}#".split("#")
    path = _resolve(files.get_file_from_path(path), page)
    return "#".join([path, anchor]) if anchor else path

# Resolve path of file relative to given page - the posixpath always includes
# one additional level of `..` which we need to remove
def _resolve(file: File, page: Page):
    path = posixpath.relpath(file.src_uri, page.file.src_uri)
    return posixpath.sep.join(path.split(posixpath.sep)[1:])

# -----------------------------------------------------------------------------

# Create badge
def _badge(icon: str, text: str = "", ty_pe: str = ""):
    classes = f"mdx-badge mdx-badge--{ty_pe}" if ty_pe else "mdx-badge"
    text = f"{text}{{ data-preview='' }}" if text.endswith(")") else text
    return "".join([
        f"<span class=\"{classes}\">",
        *([f"<span class=\"mdx-badge__icon\">{icon}</span>"] if icon else []),
        *([f"<span class=\"mdx-badge__text\">{text}</span>"] if text else []),
        "</span>",
    ])

# Create sponsors badge
def _badge_for_sponsors(page: Page, files: Files):
    icon = "material-heart"
    href = _resolve_path("insiders/index.md", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Sponsors only')",
        ty_pe = "heart"
    )

# Create badge for version
def _badge_for_version(text: str, page: Page, files: Files):
    spec = text
    path = f"changelog/index.md#{spec}"

    # Return badge
    icon = "material-tag-outline"
    href = _resolve_path("conventions.md#version", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Minimum version')",
        text = f"[{text}]({_resolve_path(path, page, files)})" if spec else ""
    )

# Create badge for version of Insiders
def _badge_for_version_insiders(text: str, page: Page, files: Files):
    spec = text.replace("insiders-", "")
    path = f"insiders/changelog/index.md#{spec}"

    # Return badge
    icon = "material-tag-heart-outline"
    href = _resolve_path("conventions.md#version-insiders", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Minimum version')",
        text = f"[{text}]({_resolve_path(path, page, files)})" if spec else ""
    )

# Create badge for feature
def _badge_for_feature(text: str, page: Page, files: Files):
    icon = "material-toggle-switch"
    href = _resolve_path("conventions.md#feature", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Optional feature')",
        text = text
    )

# Create badge for plugin
def _badge_for_plugin(text: str, page: Page, files: Files):
    icon = "material-floppy"
    href = _resolve_path("conventions.md#plugin", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Plugin')",
        text = text
    )

# Create badge for extension
def _badge_for_extension(text: str, page: Page, files: Files):
    icon = "material-language-markdown"
    href = _resolve_path("conventions.md#extension", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Markdown extension')",
        text = text
    )

# Create badge for utility
def _badge_for_utility(text: str, page: Page, files: Files):
    icon = "material-package-variant"
    href = _resolve_path("conventions.md#utility", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Third-party utility')",
        text = text
    )

# Create badge for example
def _badge_for_example(text: str):
    return "\n".join([
        _badge_for_example_download(text),
        _badge_for_example_view(text)
    ])

# Create badge for example view
def _badge_for_example_view(text: str):
    icon = "material-folder-eye"
    href = f"https://mkdocs-material.github.io/examples/{text}/"
    return _badge(
        icon = f"[:{icon}:]({href} 'View example')",
        ty_pe = "right"
    )

# Create badge for example download
def _badge_for_example_download(text: str):
    icon = "material-folder-download"
    href = f"https://mkdocs-material.github.io/examples/{text}.zip"
    return _badge(
        icon = f"[:{icon}:]({href} 'Download example')",
        text = f"[`.zip`]({href})",
        ty_pe = "right"
    )

# Create badge for default value
def _badge_for_default(text: str, page: Page, files: Files):
    icon = "material-water"
    href = _resolve_path("conventions.md#default", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Default value')",
        text = text
    )

# Create badge for empty default value
def _badge_for_default_none(page: Page, files: Files):
    icon = "material-water-outline"
    href = _resolve_path("conventions.md#default_none", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Default value is empty')"
    )

# Create badge for computed default value
def _badge_for_default_computed(page: Page, files: Files):
    icon = "material-water-check"
    href = _resolve_path("conventions.md#default_computed", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Default value is computed')"
    )

# Create badge for metadata property flag
def _badge_for_metadata(page: Page, files: Files):
    icon = "material-list-box-outline"
    href = _resolve_path("conventions.md#metadata", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Metadata property')"
    )

# Create badge for required value flag
def _badge_for_required(page: Page, files: Files):
    icon = "material-alert"
    href = _resolve_path("conventions.md#required", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Required value')"
    )

# Create badge for customization flag
def _badge_for_customization(page: Page, files: Files):
    icon = "material-brush-variant"
    href = _resolve_path("conventions.md#customization", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Customization')"
    )

# Create badge for multiple instance flag
def _badge_for_multiple(page: Page, files: Files):
    icon = "material-inbox-multiple"
    href = _resolve_path("conventions.md#multiple-instances", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Multiple instances')"
    )

# Create badge for experimental flag
def _badge_for_experimental(page: Page, files: Files):
    icon = "material-flask-outline"
    href = _resolve_path("conventions.md#experimental", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Experimental')"
    )
