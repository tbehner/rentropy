# .PHONY: build
# build:
# 	podman run --rm -v `pwd`:/io quay.io/pypa/manylinux1_x86_64 /io/build-wheels.sh

.PHONY: build
build:
	podman run --rm -v $(shell pwd):/io:Z konstin2/maturin build
