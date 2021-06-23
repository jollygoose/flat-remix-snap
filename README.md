Snap package of the [Flat Remix icon theme](https://github.com/daniruiz/flat-remix) by [daniruiz](https://github.com/daniruiz).

---

## Building snap locally

Requires
* snapcraft (```snap install snapcraft```)
* multipass (```snap install multipass```)

```sh
git clone https://github.com/jollygoose/flat-remix-gtk-snap
cd flat-remix-gtk-snap

snapcraft

# where CURRENT is the latest version of flat-remix-gtk
# and --dangerous since this local snap hasn't been verified
snap install flat-remix-gtk_CURRENT_all.snap --dangerous
```

### Applying the theme

In order to work, the snap package needs to have a '[plug](https://ubuntu.com/blog/a-guide-to-snap-permissions-and-interfaces)' 
available for either icons.

To findout which apps are able to use the icons theme, you can run:

```bash
for plug in $(snap connections | grep gtk-common-themes:icon-themes | awk '{print $2}'); do echo ${plug}; done
```

To apply to a single application

```bash
sudo snap connect NAME_OF_YOUR_APP:icon-themes flat-remix:icon-themes
```

To apply to all snaps (thanks to @flexiondotorg for the handy loop)

```bash
for plug in $(snap connections | grep gtk-common-themes:icon-themes | awk '{print $2}'); do sudo snap connect ${plug} flat-remix:icon-themes; done
```

*NOTE*: Some apps like the Ubuntu Snap Store requiring logging out and back in to load the changes.