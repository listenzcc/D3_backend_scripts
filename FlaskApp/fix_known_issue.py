# File: fix_known_issue.py
# Aim: Fix known issue of flask


class FixKnownIssue(object):
    # Fix known issue of flask
    def __init__(self):
        # Nothing to do as initial
        pass

    def pipeline(self, ext, content):
        # One stand fix of intelligent
        if ext.endswith('.html'):
            return self.pipeline_html(content)
        else:
            return content

    def pipeline_html(self, html):
        # One stand fix of .html file
        return self._ignore_header(html)

    def _ignore_header(self, html, header='<!DOCTYPE html>'):
        # Operation: Delete [header] line from html as default
        # Aim: Remove the line from the html file,
        #      otherwise the .css styles won't be correctly applied
        if html.startswith(header):
            return html[len(header):]
        return html
