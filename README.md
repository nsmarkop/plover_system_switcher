# Plover System Switcher

Command plugin for [Plover](https://github.com/openstenoproject/plover) to switch the active system.

## Installation

Download the latest version of Plover for your operating system from the [releases page](https://github.com/openstenoproject/plover/releases). Only versions 4.0.0.dev6 and higher are supported.

1. Open Plover
2. Navigate to the Plugin Manager tool
3. Select the "plover-system-switcher" plugin entry in the list
4. Click install
5. Restart Plover

The same method can be used for updating and uninstalling the plugin.

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
