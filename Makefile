HOME_ASSISTANT_HOST := homeassistant

ADDON_NAME = ohmigon
INCLUDE_FILES = Dockerfile README.md DOCS.md config.yaml run.sh src

depbuild: deploy build
	@:

deploy: test
	ssh root@${HOME_ASSISTANT_HOST} mkdir -p /addons/${ADDON_NAME}
	scp -r ${INCLUDE_FILES} root@${HOME_ASSISTANT_HOST}:/addons/${ADDON_NAME}

build:
	@echo "ha addons rebuild local_${ADDON_NAME}"
	@ssh root@${HOME_ASSISTANT_HOST} \
		"env \$$(awk '/SUPERVISOR_TOKEN/{ print \$$2 }' /etc/profile.d/homeassistant.sh) ha addons rebuild local_${ADDON_NAME}"

test:
	. .env/bin/activate && pytest

restart:
	@echo "ha addons restart local_${ADDON_NAME}"
	@ssh root@${HOME_ASSISTANT_HOST} \
		"env \$$(awk '/SUPERVISOR_TOKEN/{ print \$$2 }' /etc/profile.d/homeassistant.sh) ha addons restart local_${ADDON_NAME}"

logs:
	@echo "ha addons logs local_${ADDON_NAME}"
	@ssh root@${HOME_ASSISTANT_HOST} \
		"env \$$(awk '/SUPERVISOR_TOKEN/{ print \$$2 }' /etc/profile.d/homeassistant.sh) ha addons logs local_${ADDON_NAME}"
