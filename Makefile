engines:
	make -C engines/java8-runner
	make -C engines/pcre2-runner
	make -C engines/bru
	mkdir -p engines/re2-runner/build && cd engines/re2-runner/build && cmake -DABSL_ENABLE_INSTALL=ON .. && cmake --build . 

clean:
	make -C engines/java8-runner clean
	make -C engines/pcre2-runner clean
	make -C engines/bru clean
	rm -f engines/re2-runner/build/CMakeCache.txt
	rm -f engines/re2-runner/build/re2-runner

.PHONY: engines clean