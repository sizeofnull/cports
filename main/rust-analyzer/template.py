pkgname = "rust-analyzer"
pkgver = "2025.08.25"
_pver = pkgver.replace(".", "-")
pkgrel = 0
build_style = "cargo"
make_env = {
    "CARGO_PROFILE_RELEASE_PANIC": "unwind",
    "CFG_RELEASE": _pver,
}
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["rust-src"]
pkgdesc = "Rust compiler LSP server"
license = "Apache-2.0 OR MIT"
url = "https://github.com/rust-lang/rust-analyzer"
source = f"{url}/archive/refs/tags/{_pver}.tar.gz"
sha256 = "b48823d37f20fd9954c7105a1c0ce30c1a659319c65afa33555c59da5cee46d8"
# invokes rustfmt via rustup arg, also take longer to build than the actual
# build..
options = ["!check"]


def install(self):
    self.cargo.install(wrksrc="crates/rust-analyzer")
    self.install_license("LICENSE-MIT")
