#!/bin/bash
# delete caches and file.json


if rm file.json; then
        echo "DONE"
else
        echo "UNDONE"
fi

if rm -r __pycache__; then
        echo "DONE"
else
        echo "UNDONE"
fi

if rm -r ./models/__pycache__; then
        echo "DONE"
else
        echo "UNDONE"
fi
if rm -r ./models/engine/__pycache__; then
        echo "DONE"
else
        echo "UNDONE"
fi
if rm -r ./tests/test_models/__pycache__; then
        echo "DONE"
else
        echo "UNDONE"
fi
if rm -r ./tests/test_models/test_engine/__pycache__; then
        echo "DONE"
else
        echo "UNDONE"
fi

if rm -r ./tests/__pycache__; then
        echo "DONE"
else
        echo "UNDONE"
fi

if rm -r ./api/__pycache__; then
	echo "DONE"
else
	echo "UNDONE"
fi

if rm -r ./api/v1/views/__pycache__; then
	echo "DONE"
else
	echo "UNDONE"
fi

if rm -r ./api/v1/__pycache__; then
	echo "DONE"
else
	echo "UNDONE"
fi
