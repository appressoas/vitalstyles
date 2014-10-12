#!/usr/bin/env python

from vitalstyles.settings import Settings
from vitalstyles.cli import cli


class CustomSettings(Settings):
    def setup_without_settingsfile(self):
        self.settings.update({
            "preview_cssfile": "styles.css",
            "title": "My style guide built using custom settings object",
            "inpaths": [
                "less"
            ],
            "asset_directories": [
                "styleguide_assets"
            ],
            'include_stock_assets': True
        })

if __name__ == '__main__':
    cli(settingsobject=CustomSettings())
