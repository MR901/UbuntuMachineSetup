.PHONY: act_env_office act_env_personal  run_jupyter_notebook run_redis_server run_redis_cli run_mongodb_server run_mongodb_cli

SHELL := /bin/bash
# default is /bin/sh which doesn't import source

TEST_PATH=./

act_env_office:
	source activate_office_virtual_env.sh
# https://stackoverflow.com/questions/7369145/activating-a-virtualenv-using-a-shell-script-doesnt-seem-to-work
# https://stackoverflow.com/questions/7507810/how-to-source-a-script-in-a-makefile/7508273


act_env_personal:
	source /Users/mohitrajput/Documents/VirtualEnvironments/MyPersonalVirtEnv/bin/activate

run_jupyter_notebook:
	jupyter notebook

run_redis_server:
	redis-server &

run_redis_cli:
	redis-cli

run_mongodb_server:
	mongod --config /usr/local/etc/mongod.conf &
# https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/

run_mongodb_cli:
	mongo