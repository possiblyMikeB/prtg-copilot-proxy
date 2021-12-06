
METRIC_PREFIX=(kernel 
	       disk
	       filesys
	       swap
	       mem
	       network
	       ipc
	       vfs
	       sysfs
	       tmpfs
	       containers
	       nvidia
	       nfs4
	       cgroup
	       acct
	       kvm)

echo "# _Some_ Of The Available Metrics" > METRICS.md

echo "## Metric Group Quicklinks" >> METRICS.md
for prefix in ${METRIC_PREFIX[*]}; do
    echo " * [$prefix](#$prefix)" >> METRICS.md
done

echo "## Metric Descriptions" >> METRICS.md
for prefix in ${METRIC_PREFIX[*]}; do
    echo "### ${prefix}" >> METRICS.md 
    pminfo -T $prefix | \
	sed -e 's/^\([a-z0-9A-Z][A-Za-z0-9_.]\+[A-Za-z0-9]\)$/#### \1/' \
	    -e 's/^Help:$//' \
	>> METRICS.md

done
