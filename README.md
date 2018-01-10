# Plover System Switcher

Command plugin for [Plover](https://github.com/openstenoproject/plover) to switch the active system.

## Installation

*This plugin has not been released on PyPI yet, so locally installing from source is currently the only option.*

Download the latest version of Plover for your operating system from the [releases page](https://github.com/openstenoproject/plover/releases). Only versions 4.0.0.dev6 and higher are supported.

Once installed, navigate to the Plugin Manager in the main Plover window. From there you should see the "plover-system-switcher" plugin which you can select and install to use after restarting Plover. The same method can be used for updating and uninstalling the plugin.

If you run Plover from source you can alternatively install it directly with pip or you can check out a copy of this repository and install it locally with pip like so::

``` bash
pip install -e /path/to/repo
```

## Usage

In order to use this plugin you just need to create a dictionary entry of the form:

``` json
{
    "example_stroke": "{PLOVER:SWITCH_SYSTEM:system name}"
}
```

For example, if you were in a non-English system you could switch to English with the following:

``` json
{
    "example_stroke": "{PLOVER:SWITCH_SYSTEM:English Stenotype}"
}
```
