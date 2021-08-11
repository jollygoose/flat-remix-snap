Snap package of the [Flat Remix icon theme](https://github.com/daniruiz/flat-remix) by [@daniruiz](https://github.com/daniruiz).

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/flat-remix)

---

## Attributions

All credit goes to the developers of the Flat Remix project.
https://github.com/daniruiz/flat-remix

## Building the snap locally

Requires
* [snapcraft](https://snapcraft.io/snapcraft) (```snap install snapcraft```)
* [multipass](https://snapcraft.io/multipass) (```snap install multipass```)

```sh
git clone https://github.com/jollygoose/flat-remix-snap
cd flat-remix-snap

snapcraft

# where [current-version] is the latest version/release of in the in snapcraft.yaml file.
# The --dangerous is used since this snap was built locally and does not originate from the snap store
snap install flat-remix_[current-version]_all.snap --dangerous
```

## Applying the theme

In order to work, the snap package needs to have a '[plug](https://ubuntu.com/blog/a-guide-to-snap-permissions-and-interfaces)' 
available for either 'icon-themes'.

To apply the theme to a single application:

```bash
sudo snap connect [snap-you-want-to-theme]:icon-themes flat-remix:icon-themes
```

To apply the theme to all snaps (thanks to @flexiondotorg for the handy loop):

```bash
for plug in $(snap connections | grep gtk-common-themes:icon-themes | awk '{print $2}'); do sudo snap connect ${plug} flat-remix:icon-themes; done
```

*NOTE*: Some apps (like the Ubuntu Snap Store) may require logging out, and back in to load the changes.