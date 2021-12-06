# _Some_ Available Metrics
 * [kernel](#kernel)
 * [disk](#disk)
 * [filesys](#filesys)
 * [swap](#swap)
 * [mem](#mem)
 * [network](#network)
 * [ipc](#ipc)
 * [vfs](#vfs)
 * [sysfs](#sysfs)
 * [tmpfs](#tmpfs)
 * [containers](#containers)
 * [nvidia](#nvidia)
 * [nfs4](#nfs4)
 * [cgroup](#cgroup)
 * [acct](#acct)
 * [kvm](#kvm)
## kernel

### kernel.all.load

1, 5 and 15 minute load average

### kernel.all.intr

The value is the first value from the intr field in /proc/stat,
which is a counter of the total number of interrupts processed.
The value is normally converted to a rate (count/second).
This counter usually increases by at least HZ/second,
i.e. the clock interrupt rate, wehich is usually 100/second.

See also kernel.percpu.intr and kernel.percpu.interrupts to get
the breakdown of interrupt count by interrupt type and which CPU
processed each one.

### kernel.all.pswitch

context switches metric from /proc/stat

### kernel.all.sysfork

fork rate metric from /proc/stat

### kernel.all.running

number of currently running processes from /proc/stat

### kernel.all.blocked

number of currently blocked processes from /proc/stat

### kernel.all.boottime

boot time from /proc/stat

### kernel.all.hz

value of HZ (jiffies/second) for the currently running kernel

### kernel.all.uptime

time the current kernel has been running

### kernel.all.idletime

time the current kernel has been idle since boot

### kernel.all.nusers

number of user sessions on the system (including root)

### kernel.all.nroots

number of root user sessions on the system (only root)

### kernel.all.nsessions

number of utmp sessions (login records)

### kernel.all.lastpid

most recently allocated process identifier

### kernel.all.runnable

total number of processes in the (per-CPU) run queues

### kernel.all.nprocs

total number of processes (lightweight)

### kernel.all.pid_max

maximum process identifier from /proc/sys/kernel/pid_max

### kernel.all.nptys

number of in-use pseudo-ttys from /proc/sys/kernel/pty/nr

### kernel.all.cpu.user

total user CPU time from /proc/stat for all CPUs, including guest CPU time

### kernel.all.cpu.nice

total nice user CPU time from /proc/stat for all CPUs, including guest time

### kernel.all.cpu.sys

total sys CPU time from /proc/stat for all CPUs

### kernel.all.cpu.idle

total idle CPU time from /proc/stat for all CPUs

### kernel.all.cpu.intr

Total time spent processing interrupts on all CPUs.
This value includes both soft and hard interrupt processing time.

### kernel.all.cpu.steal

Total CPU time when a CPU had a runnable process, but the hypervisor
(virtualisation layer) chose to run something else instead.

### kernel.all.cpu.guest

Total CPU time spent running virtual guest operating systems.

### kernel.all.cpu.vuser

total user CPU time from /proc/stat for all CPUs, excluding guest CPU time

### kernel.all.cpu.guest_nice

Total CPU nice time spent running virtual guest operating systems.

### kernel.all.cpu.vnice

total nice user CPU time from /proc/stat for all CPUs, excluding guest time

### kernel.all.cpu.wait.total

total wait CPU time from /proc/stat for all CPUs

### kernel.all.cpu.irq.soft

Total soft interrupt CPU time (deferred interrupt handling code,
not run in the initial interrupt handler).

### kernel.all.cpu.irq.hard

Total hard interrupt CPU time ("hard" interrupt handling code
is the code run directly on receipt of the initial hardware
interrupt, and does not include "soft" interrupt handling code
which is deferred until later).

### kernel.all.interrupts.total

Aggregated interrupt counts for each type of interrupt reported
by the kernel in /proc/interrupts.

### kernel.all.interrupts.missed

MIS count from /proc/interrupts

### kernel.all.interrupts.errors

This is a global counter (normally converted to a count/second)
for any and all errors that occur while handling interrupts.

### kernel.all.softirqs.total

Aggregated interrupt counts for each type of interrupt reported
by the kernel in /proc/softirqs.

### kernel.all.entropy.avail

entropy available to random number generators

### kernel.all.entropy.poolsize

maximum size of the entropy pool

### kernel.all.pressure.cpu.some.avg

Indicates the time in which at least some tasks stalled on CPU resources.
The ratios are tracked as recent trends over ten second, one minute,
and five minute windows.
Pressure stall information (PSI) from /proc/pressure/cpu.

### kernel.all.pressure.cpu.some.total

Indicates the time in which at least some tasks stalled on CPU resources.
Pressure stall information (PSI) from /proc/pressure/cpu.

### kernel.all.pressure.memory.some.avg

Indicates the time in which at least some tasks stalled on memory resources.
The ratios are tracked as recent trends over ten second, one minute,
and five minute windows.
Pressure stall information (PSI) from /proc/pressure/memory.

### kernel.all.pressure.memory.some.total

The CPU time for which at least some tasks stalled on memory resources.
Pressure stall information (PSI) from /proc/pressure/memory.

### kernel.all.pressure.memory.full.avg

Indicates the time in which all tasks stalled on memory resources.
The ratios are tracked as recent trends over ten second, one minute,
and five minute windows.
Pressure stall information (PSI) from /proc/pressure/memory.

### kernel.all.pressure.memory.full.total

The CPU time for which all tasks stalled on memory resources.
Pressure stall information (PSI) from /proc/pressure/memory.

### kernel.all.pressure.io.some.avg

Indicates the time in which at least some tasks stalled on IO resources.
The ratios are tracked as recent trends over ten second, one minute,
and five minute windows.
Pressure stall information (PSI) from /proc/pressure/io.

### kernel.all.pressure.io.some.total

The CPU time in which at least some tasks stalled on IO resources.
Pressure stall information (PSI) from /proc/pressure/io.

### kernel.all.pressure.io.full.avg

Indicates the time in which all tasks stalled on IO resources.
The ratios are tracked as recent trends over ten second, one minute,
and five minute windows.
Pressure stall information (PSI) from /proc/pressure/io.

### kernel.all.pressure.io.full.total

The CPU time in which all tasks stalled on IO resources.
Pressure stall information (PSI) from /proc/pressure/io.

### kernel.percpu.interrupts

Counts of each interrupt type, for each CPU.

### kernel.percpu.softirqs

per CPU per soft interrupt counts from /proc/softirqs

### kernel.percpu.intr

Aggregate count of each CPUs interrupt processing count, calculated
as the sum of all interrupt types in /proc/interrupts for each CPU.

### kernel.percpu.sirq

per CPU aggregate soft interrupt counts from /proc/softirqs

### kernel.percpu.cpu.user

percpu user CPU time metric from /proc/stat, including guest CPU time

### kernel.percpu.cpu.nice

percpu nice user CPU time metric from /proc/stat, including guest CPU time

### kernel.percpu.cpu.sys

percpu sys CPU time metric from /proc/stat

### kernel.percpu.cpu.idle

percpu idle CPU time metric from /proc/stat

### kernel.percpu.cpu.intr

Total time spent processing interrupts on each CPU (this includes
both soft and hard interrupt processing time).

### kernel.percpu.cpu.steal

Per-CPU time when the CPU had a runnable process, but the hypervisor
(virtualisation layer) chose to run something else instead.

### kernel.percpu.cpu.guest

Per-CPU time spent running (virtual) guest operating systems.

### kernel.percpu.cpu.vuser

percpu user CPU time metric from /proc/stat, excluding guest CPU time

### kernel.percpu.cpu.guest_nice

Per-CPU nice time spent running (virtual) guest operating systems.

### kernel.percpu.cpu.vnice

percpu nice user CPU time metric from /proc/stat, excluding guest CPU time

### kernel.percpu.cpu.wait.total

Per-CPU I/O wait CPU time - time spent with outstanding I/O requests.

### kernel.percpu.cpu.irq.soft

Per-CPU soft interrupt CPU time (deferred interrupt handling code,
not run in the initial interrupt handler).

### kernel.percpu.cpu.irq.hard

Per-CPU hard interrupt CPU time ("hard" interrupt handling code
is the code run directly on receipt of the initial hardware
interrupt, and does not include "soft" interrupt handling code
which is deferred until later).

### kernel.pernode.cpu.user

total user CPU time from /proc/stat for each node, including guest CPU time

### kernel.pernode.cpu.nice

total nice user CPU time from /proc/stat for each node, including guest time

### kernel.pernode.cpu.sys

total sys CPU time from /proc/stat for each node

### kernel.pernode.cpu.idle

total idle CPU time from /proc/stat for each node

### kernel.pernode.cpu.intr

total interrupt CPU time from /proc/stat for each node

### kernel.pernode.cpu.steal

total virtualisation CPU steal time for each node

### kernel.pernode.cpu.guest

total virtual guest CPU time for each node

### kernel.pernode.cpu.vuser

total user CPU time from /proc/stat for each node, excluding guest CPU time

### kernel.pernode.cpu.guest_nice

total virtual nice guest CPU time for each node

### kernel.pernode.cpu.vnice

total nice user CPU time from /proc/stat for each node, excluding guest time

### kernel.pernode.cpu.wait.total

total wait CPU time from /proc/stat for each node

### kernel.pernode.cpu.irq.soft

soft interrupt CPU time from /proc/stat for each node

### kernel.pernode.cpu.irq.hard

hard interrupt CPU time from /proc/stat for each node

### kernel.uname.release

Release level of the running kernel as reported via the release[]
value returned from uname(2) or uname -r.

See also pmda.uname.

### kernel.uname.version

Version level of the running kernel as reported by the version[]
value returned from uname(2) or uname -v.  Usually a build number
followed by a build date.

See also pmda.uname.

### kernel.uname.sysname

Name of the implementation of the running operating system as reported
by the sysname[] value returned from uname(2) or uname -s.  Usually
"Linux".

See also pmda.uname.

### kernel.uname.machine

Name of the hardware type the system is running on as reported by the machine[]
value returned from uname(2) or uname -m, e.g. "i686".

See also pmda.uname.

### kernel.uname.nodename

Name of this node on the network as reported by the nodename[]
value returned from uname(2) or uname -n.  Usually a synonym for
the host name.

See also pmda.uname.

### kernel.uname.distro

The Linux distribution name, as determined by a number of heuristics.
For example:
+ on Fedora, the contents of /etc/fedora-release
+ on RedHat, the contents of /etc/redhat-release

### kernel.cpu.util.user

percentage of user time across all CPUs, including guest CPU time

### kernel.cpu.util.nice

percentage of nice user time across all CPUs, including guest nice CPU time

### kernel.cpu.util.sys

percentage of sys time across all CPUs

### kernel.cpu.util.idle

percentage of idle time across all CPUs

### kernel.cpu.util.intr

Percentage of time spent processing interrupts across all CPUs.
This value includes both soft and hard interrupt processing time.

### kernel.cpu.util.wait

percentage of wait time across all CPUs

### kernel.cpu.util.steal

Percentage of time across all CPUs when a CPU had a runnable process,
but the hypervisor (virtualisation layer) chose to run something else
instead.
## disk

### disk.dev.read

Cumulative number of disk read operations since system boot time (subject
to counter wrap).

### disk.dev.write

Cumulative number of disk write operations since system boot time (subject
to counter wrap).

### disk.dev.total

Cumulative number of disk read and write operations since system boot
time (subject to counter wrap).

### disk.dev.blkread

Cumulative number of disk block read operations since system boot time
(subject to counter wrap).

### disk.dev.blkwrite

Cumulative number of disk block write operations since system boot time
(subject to counter wrap).

### disk.dev.blktotal

Cumulative number of disk block read and write operations since system
boot time (subject to counter wrap).

### disk.dev.read_bytes

per-disk count of bytes read

### disk.dev.write_bytes

per-disk count of bytes written

### disk.dev.total_bytes

per-disk count of total bytes read and written

### disk.dev.read_merge

Count of read requests that were merged with an already queued read request.

### disk.dev.write_merge

Count of write requests that were merged with an already queued write request.

### disk.dev.avactive

Counts the number of milliseconds for which at least one I/O is in
progress for each device.

When converted to a rate, this metric represents the average utilization of
the disk during the sampling interval.  A value of 0.5 (or 50%) means the
disk was active (i.e. busy) half the time.

### disk.dev.read_rawactive

For each completed read on each disk the response time (queue time plus
service time) in milliseconds is added to the associated instance of
this metric.

When converted to a normalized rate, the value represents the time average
of the number of outstanding reads for a disk.  When divided by the number
of completed reads for a disk (disk.dev.read), the value represents the
stochastic average of the read response (or wait) time for that disk.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.dev.r_await = delta(disk.dev.read_rawactive) / delta(disk.dev.read)

### disk.dev.write_rawactive

For each completed write on each disk the response time (queue time plus
service time) in milliseconds is added to the associated instance of
this metric.

When converted to a normalized rate, the value represents the time
average of the number of outstanding writes for a disk.  When divided by
the number of completed writes for a disk (disk.dev.write), the value
represents the stochastic average of the write response (or wait)
time for that disk.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.dev.w_await = delta(disk.dev.write_rawactive) / delta(disk.dev.write)

### disk.dev.total_rawactive

For each completed I/O on each disk the response time (queue time plus
service time) in milliseconds is added to the associated instance of
this metric.

When converted to a normalized rate, the value represents the time average
of the number of outstanding I/Os for a disk.  When divided by the number
of completed I/Os for a disk (disk.dev.total), the value represents the
stochastic average of the I/O response (or wait) time for that disk.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.dev.await = delta(disk.dev.total_rawactive) / delta(disk.dev.total)

### disk.dev.aveq

When converted to a rate, this metric represents the time averaged disk
request queue length during the sampling interval.  A value of 2.5 (or 250%)
represents a time averaged queue length of 2.5 requests during the sampling
interval.

### disk.dev.scheduler

The name of the I/O scheduler in use for each device.  The scheduler
is part of the block layer in the kernel, and attempts to optimise the
I/O submission patterns using various techniques (typically, sorting
and merging adjacent requests into larger ones to reduce seek activity,
but certainly not limited to that).

### disk.dev.capacity

Total space presented by each block device, from /proc/partitions.

### disk.dev.discard

Cumulative number of disk discard operations since system boot time.

### disk.dev.blkdiscard

Cumulative number of disk block discard operations since system boot time.

### disk.dev.discard_bytes

per-disk count of bytes discard'ed

### disk.dev.discard_merge

Count of discard requests that were merged with an already queued discard
request.

### disk.dev.discard_rawactive

For each completed discard on each disk the response time (queue time plus
service time) in milliseconds is added to the associated instance of
this metric.
It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.dev.d_await = delta(disk.dev.discard_rawactive) / delta(disk.dev.discard)

### disk.dev.flush

per-disk flush operations

### disk.dev.flush_rawactive

For each completed flush on each disk the response time (queue time plus
service time) in milliseconds is added to the associated instance of
this metric.
It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.dev.f_await = delta(disk.dev.flush_rawactive) / delta(disk.dev.flush)

### disk.all.read

Cumulative number of disk read operations since system boot time
(subject to counter wrap), summed over all disk devices.

### disk.all.write

Cumulative number of disk read operations since system boot time
(subject to counter wrap), summed over all disk devices.

### disk.all.total

Cumulative number of disk read and write operations since system boot
time (subject to counter wrap), summed over all disk devices.

### disk.all.blkread

Cumulative number of disk block read operations since system boot time
(subject to counter wrap), summed over all disk devices.

### disk.all.blkwrite

Cumulative number of disk block write operations since system boot time
(subject to counter wrap), summed over all disk devices.

### disk.all.blktotal

Cumulative number of disk block read and write operations since system
boot time (subject to counter wrap), summed over all disk devices.

### disk.all.read_bytes

count of bytes read for all disk devices

### disk.all.write_bytes

count of bytes written for all disk devices

### disk.all.total_bytes

total count of bytes read and written for all disk devices

### disk.all.read_merge

Total count of read requests that were merged with an already queued read request.

### disk.all.write_merge

Total count of write requests that were merged with an already queued write request.

### disk.all.avactive

Counts the number of milliseconds for which at least one I/O is in
progress on each disk, summed across all disks.

When converted to a rate and divided by the number of disks (hinv.ndisk),
this metric represents the average utilization of all disks during the
sampling interval.  A value of 0.25 (or 25%) means that on average every
disk was active (i.e. busy) one quarter of the time.

### disk.all.read_rawactive

For each completed read on every disk the response time (queue time plus
service time) in milliseconds is added to this metric.

When converted to a normalized rate, the value represents the time average
of the number of outstanding reads across all disks.  When divided
by the number of completed reads for all disks (disk.all.read), value
represents the stochastic average of the read response (or wait) time
across all disks.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.all.r_await = delta(disk.all.read_rawactive) / delta(disk.all.read)

### disk.all.write_rawactive

For each completed write on every disk the response time (queue time
plus service time) in milliseconds is added to this metric.

When converted to a normalized rate, the value represents the time average
of the number of outstanding writes across all disks.  When divided by
the number of completed writes for all disks (disk.all.write), value
represents the stochastic average of the write response (or wait) time
across all disks.

### disk.all.total_rawactive

For each completed I/O on every disk the response time (queue time
plus service time) in milliseconds is added to this metric.

When converted to a normalized rate, the value represents the time average
of the number of outstanding I/Os across all disks.  When divided by
the number of completed I/Os for all disks (disk.all.total), value
represents the stochastic average of the I/O response (or wait) time
across all disks.

### disk.all.aveq

When converted to a rate, this metric represents the average across all disks
of the time averaged request queue length during the sampling interval.
A value of 1.5 (or 150%) suggests that (on average) over all disks there was
a time averaged queue length of 1.5 requests during the sampling interval.

### disk.all.discard

total discard operations, summed for all disks

### disk.all.blkdiscard

block discard operations, summed for all disks

### disk.all.discard_bytes

count of discard bytes for all disk devices

### disk.all.discard_merge

Total count of discard requests that were merged with an already queued
discard request.

### disk.all.discard_rawactive

For each discard on every disk the response time (queue time plus
service time) in milliseconds is added to this metric.

When converted to a normalized rate, the value represents the time average
of the number of outstanding discards across all disks.  When divided
by the number of completed discards for all disks (disk.all.discard), the
value represents the stochastic average of the discard response (or wait)
time across all disks.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.all.d_await = delta(disk.all.discard_rawactive) / delta(disk.all.discard)

### disk.all.flush

total flush operations, summed for all disks

### disk.all.flush_rawactive

For each flush on every disk the response time (queue time plus
service time) in milliseconds is added to this metric.

When converted to a normalized rate, the value represents the time average
of the number of outstanding flushes across all disks.  When divided
by the number of completed flushes for all disks (disk.all.flush), the
value represents the stochastic average of the flush response (or wait)
time across all disks.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.all.f_await = delta(disk.all.flush_rawactive) / delta(disk.all.flush)

### disk.partitions.read

Cumulative number of disk read operations since system boot time
(subject to counter wrap) for individual disk partitions or logical
volumes.

### disk.partitions.write

Cumulative number of disk write operations since system boot time
(subject to counter wrap) for individual disk partitions or logical
volumes.

### disk.partitions.total

Cumulative number of disk read and write operations since system boot
time (subject to counter wrap) for individual disk partitions or
logical volumes.

### disk.partitions.blkread

Cumulative number of disk block read operations since system boot time
(subject to counter wrap) for individual disk partitions or logical
volumes.

### disk.partitions.blkwrite

Cumulative number of disk block write operations since system boot time
(subject to counter wrap) for individual disk partitions or logical
volumes.

### disk.partitions.blktotal

Cumulative number of disk block read and write operations since system
boot time (subject to counter wrap) for individual disk partitions or
logical volumes.

### disk.partitions.read_bytes

Cumulative number of bytes read since system boot time (subject to
counter wrap) for individual disk partitions or logical volumes.

### disk.partitions.write_bytes

Cumulative number of bytes written since system boot time (subject to
counter wrap) for individual disk partitions or logical volumes.

### disk.partitions.total_bytes

Cumulative number of bytes read and written since system boot time
(subject to counter wrap) for individual disk partitions or logical
volumes.

### disk.partitions.read_merge

per-disk-partition count of merged read requests

### disk.partitions.write_merge

per-disk-partition count of merged write requests

### disk.partitions.avactive

Counts the number of milliseconds for which at least one I/O is in
progress for each disk partition.

When converted to a rate, this metric represents the average utilization
of the disk partition during the sampling interval.  A value of 0.5
(or 50%) means the disk partition was active (i.e. busy) half the time.

### disk.partitions.aveq

per-disk-partition device time averaged count of request queue length

### disk.partitions.read_rawactive

For each completed read on each disk partition the response time
(queue time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time average
of the number of outstanding reads for a disk partition.  When divided by
the number of completed reads for a disk partition (disk.partitions.read),
the value represents the stochastic average of the read response (or wait)
time for that disk partition.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.partitions.r_await = delta(disk.partitions.read_rawactive) /
                             delta(disk.partitions.read)

### disk.partitions.write_rawactive

For each completed write on each disk partition the response time
(queue time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time
average of the number of outstanding writes for a disk partition.
When divided by the number of completed writes for a disk partition
(disk.partitions.write), the value represents the stochastic average of
the write response (or wait) time for that disk partition.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.partitions.w_await = delta(disk.partitions.write_rawactive) /
                             delta(disk.partitions.write)

### disk.partitions.total_rawactive

For each completed I/O on each disk partition the response time (queue
time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time
average of the number of outstanding I/Os for a disk partition.
When divided by the number of completed I/Os for a disk partition
(disk.partitions.total), the value represents the stochastic average of
the I/O response (or wait) time for that disk partition.

### disk.partitions.capacity

Total space presented by each disk partition, from /proc/partitions.

### disk.partitions.discard

discard operations count for storage partitions

### disk.partitions.blkdiscard

block discard operations count for storage partitions

### disk.partitions.discard_bytes

number of discard bytes for storage partitions

### disk.partitions.discard_merge

per-disk-partition count of merged discard requests

### disk.partitions.discard_rawactive

For each completed discard on each disk partition the response time
(queue time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time average
of the number of outstanding discards for a disk partition.  When divided by
the number of completed discards for a disk partition (disk.partitions.discard),
the value represents the stochastic average of the discard response (or wait)
time for that disk partition.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.partitions.d_await = delta(disk.partitions.discard_rawactive) /
                             delta(disk.partitions.discard)

### disk.partitions.flush

flush operations metric for storage partitions

### disk.partitions.flush_rawactive

For each completed flush on each disk partition the response time
(queue time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time average
of the number of outstanding flushes for a disk partition.  When divided by
the number of completed flushes for a disk partition (disk.partitions.flush),
the value represents the stochastic average of the flush response (or wait)
time for that disk partition.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.partitions.f_await = delta(disk.partitions.flush_rawactive) /
                             delta(disk.partitions.flush)

### disk.dm.read

per-device-mapper device read operations

### disk.dm.write

per-device-mapper device write operations

### disk.dm.total

per-device-mapper device total (read+write) operations

### disk.dm.blkread

per-device-mapper device block read operations

### disk.dm.blkwrite

per-device-mapper device block write operations

### disk.dm.blktotal

per-device-mapper device total (read+write) block operations

### disk.dm.read_bytes

per-device-mapper device count of bytes read

### disk.dm.write_bytes

per-device-mapper device count of bytes written

### disk.dm.total_bytes

per-device-mapper device count of total bytes read and written

### disk.dm.read_merge

per-device-mapper device count of merged read requests

### disk.dm.write_merge

per-device-mapper device count of merged write requests

### disk.dm.avactive

Counts the number of milliseconds for which at least one I/O is in
progress for each device-mapper device.

When converted to a rate, this metric represents the average utilization
of the device during the sampling interval.  A value of 0.5 (or 50%)
means the device was active (i.e. busy) half the time.

### disk.dm.aveq

per-device-mapper device time averaged count of request queue length

### disk.dm.read_rawactive

For each completed read on each device-mapper device the response time
(queue time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time
average of the number of outstanding reads for a device-mapper device.
When divided by the number of completed reads for a device-mapper device
(disk.dm.read), the value represents the stochastic average of the read
response (or wait) time for that device.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.dm.r_await = delta(disk.dm.read_rawactive) / delta(disk.dm.read)

### disk.dm.write_rawactive

For each completed write on each device-mapper device the response time
(queue time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time
average of the number of outstanding writes for a device-mapper device.
When divided by the number of completed writes for a device-mapper device
(disk.dm.write), the value represents the stochastic average of the
write response (or wait) time for that device.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.dm.w_await = delta(disk.dm.write_rawactive) / delta(disk.dm.write)

### disk.dm.total_rawactive

For each completed I/O on each device-mapper device the response time
(queue time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time
average of the number of outstanding I/Os for a device-mapper device.
When divided by the number of completed I/Os for a device-mapper device
(disk.dm.total), the value represents the stochastic average of the I/O
response (or wait) time for that device-mapper device.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.dm.await = delta(disk.dm.total_rawactive) / delta(disk.dm.total)

### disk.dm.capacity

Total space presented by each device mapper device, from /proc/partitions.

### disk.dm.discard

per-device-mapper device discard operations

### disk.dm.blkdiscard

per-device-mapper device block discard operations

### disk.dm.discard_bytes

per-device-mapper device count of discard bytes

### disk.dm.discard_merge

per-device-mapper device count of merged discard requests

### disk.dm.discard_rawactive

For each completed discard on each device-mapper device the response time
(queue time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time
average of the number of outstanding discards for a device-mapper device.
When divided by the number of completed discards for a device-mapper device
(disk.dm.discards), the value represents the stochastic average of the
discard response (or wait) time for that device.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.dm.d_await = delta(disk.dm.discard_rawactive) / delta(disk.dm.discard)

### disk.dm.flush

per-device-mapper device flush operations

### disk.dm.flush_rawactive

For each completed flush on each device-mapper device the response time
(queue time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time
average of the number of outstanding flushes for a device-mapper device.
When divided by the number of completed flushes for a device-mapper device
(disk.dm.flush), the value represents the stochastic average of the flush
response (or wait) time for that device.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.dm.f_await = delta(disk.dm.flush_rawactive) / delta(disk.dm.flush)

### disk.md.read

per-multi-device device read operations

### disk.md.write

per-multi-device device write operations

### disk.md.total

per-multi-device device total (read+write) operations

### disk.md.blkread

per-multi-device device block read operations

### disk.md.blkwrite

per-multi-device device block write operations

### disk.md.blktotal

per-multi-device device total (read+write) block operations

### disk.md.read_bytes

per-multi-device device count of bytes read

### disk.md.write_bytes

per-multi-device device count of bytes written

### disk.md.total_bytes

per-multi-device device count of total bytes read and written

### disk.md.read_merge

per-multi-device device count of merged read requests

### disk.md.write_merge

per-multi-device device count of merged write requests

### disk.md.avactive

Counts the number of milliseconds for which at least one I/O is in
progress for each multi-device device.

When converted to a rate, this metric represents the average utilization
of the device during the sampling interval.  A value of 0.5 (or 50%)
means the device was active (i.e. busy) half the time.

### disk.md.aveq

per-multi-device device time averaged count of request queue length

### disk.md.read_rawactive

For each completed read on each multi-device device the response time
(queue time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time
average of the number of outstanding reads for a multi-device device.
When divided by the number of completed reads for a multi-device device
(disk.md.read), the value represents the stochastic average of the read
response (or wait) time for that device.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.md.r_await = delta(disk.md.read_rawactive) / delta(disk.md.read)

### disk.md.write_rawactive

For each completed write on each multi-device device the response time
(queue time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time
average of the number of outstanding writes for a multi-device device.
When divided by the number of completed writes for a multi-device device
(disk.md.write), the value represents the stochastic average of the
write response (or wait) time for that device.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.md.w_await = delta(disk.md.write_rawactive) / delta(disk.md.write)

### disk.md.total_rawactive

For each completed I/O on each multi-device device the response time
(queue time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time
average of the number of outstanding I/Os for a multi-device device.
When divided by the number of completed I/Os for a multi-device device
(disk.md.total), the value represents the stochastic average of the I/O
response (or wait) time for that multi-device device.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.md.await = delta(disk.md.total_rawactive) / delta(disk.md.total)

### disk.md.status

per-multi-device "mdadm --test --detail <device>" return code

### disk.md.capacity

Total space presented by each multi-device device, from /proc/partitions.

### disk.md.discard

per-multi-device device discard operations

### disk.md.blkdiscard

per-multi-device device block discard operations

### disk.md.discard_bytes

per-multi-device device count of discard bytes

### disk.md.discard_merge

per-multi-device device count of merged discard requests

### disk.md.discard_rawactive

For each completed discard on each multi-device device the response time
(queue time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time
average of the number of outstanding discards for a multi-device device.
When divided by the number of completed discards for a multi-device device
(disk.md.discards), the value represents the stochastic average of the
discard response (or wait) time for that device.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.md.d_await = delta(disk.md.discard_rawactive) / delta(disk.md.discard)

### disk.md.flush

per-multi-device device flush operations

### disk.md.flush_rawactive

For each completed flush on each multi-device device the response time
(queue time plus service time) in milliseconds is added to the associated
instance of this metric.

When converted to a normalized rate, the value represents the time
average of the number of outstanding flushes for a multi-device device.
When divided by the number of completed flushes for a multi-device device
(disk.md.flush), the value represents the stochastic average of the flush
response (or wait) time for that device.

It is suitable mainly for use in calculations with other metrics,
e.g. mirroring the results from existing performance tools:

 iostat.md.f_await = delta(disk.md.flush_rawactive) / delta(disk.md.flush)

### disk.dev.await

average time in milliseconds that read and write requests
were queued (and serviced) during the reporting interval.

### disk.dev.r_await

average time in milliseconds that read requests were queued
(and serviced) during the reporting interval.

### disk.dev.w_await

average time in milliseconds that write requests were queued
(and serviced) during the reporting interval.

### disk.dev.d_await

average time in milliseconds that discard requests were queued
(and serviced) during the reporting interval.

### disk.dev.f_await

average time in milliseconds that flush requests were queued
(and serviced) during the reporting interval.

### disk.dev.avg_qlen

average read and write I/O queue length to the device during the reporting interval.

### disk.dev.avg_rqsz

average I/O request size for both reads and writes during the reporting interval.

### disk.dev.r_avg_rqsz

average I/O request size for reads to the device during the reporting interval.

### disk.dev.w_avg_rqsz

average I/O request size for writes to the device during the reporting interval.

### disk.dev.d_avg_rqsz

average I/O request size for discards to the device during the reporting interval.

### disk.dev.util

The percentage of time during the reporting interval that the
device was busy processing requests (reads and writes). A value
of 100% indicates device saturation.

### disk.dm.await

average time in milliseconds that read and write requests
were queued (and serviced) to the device-mapper logical
device during the reporting interval.

### disk.dm.r_await

average time in milliseconds that read requests were queued
(and serviced) to the device-mapper logical device during
the reporting interval.

### disk.dm.w_await

average time in milliseconds that write requests were queued
(and serviced) to the device-mapper logical device during
the reporting interval.

### disk.dm.d_await

average time in milliseconds that discard requests were queued
(and serviced) to the device-mapper logical device during
the reporting interval.

### disk.dm.f_await

average time in milliseconds that flush requests were queued
(and serviced) to the device-mapper logical device during
the reporting interval.

### disk.dm.avg_qlen

average read and write I/O queue length to the device-mapper logical
device during the reporting interval.

### disk.dm.avg_rqsz

average I/O request size for reads and writes to the device-mapper logical
device during the reporting interval.

### disk.dm.r_avg_rqsz

average I/O request size for reads to the device-mapper logical device
during the reporting interval.

### disk.dm.w_avg_rqsz

average I/O request size for writes to the device-mapper logical device
during the reporting interval.

### disk.dm.d_avg_rqsz

average I/O request size for discards to the device-mapper logical device
during the reporting interval.

### disk.dm.util

The percentage of time during the reporting interval that the
device-mapper logical device was busy processing requests (reads
and writes). A value of 100% indicates device saturation.

### disk.md.await

average time in milliseconds that read and write requests
were queued (and serviced) to the per-multi-device logical
device during the reporting interval.

### disk.md.r_await

average time in milliseconds that read requests were queued
(and serviced) to the per-multi-device logical device during
the reporting interval.

### disk.md.w_await

average time in milliseconds that write requests were queued
(and serviced) to the per-multi-device logical device during
the reporting interval.

### disk.md.d_await

average time in milliseconds that discard requests were queued
(and serviced) to the per-multi-device logical device during
the reporting interval.

### disk.md.f_await

average time in milliseconds that flush requests were queued
(and serviced) to the per-multi-device logical device during
the reporting interval.

### disk.md.avg_qlen

average read and write I/O queue length to the per-multi-device logical
device during the reporting interval.

### disk.md.avg_rqsz

average I/O request size for reads and writes to the per-multi-device logical
device during the reporting interval.

### disk.md.r_avg_rqsz

average I/O request size for reads to the per-multi-device logical device
during the reporting interval.

### disk.md.w_avg_rqsz

average I/O request size for writes to the per-multi-device logical device
during the reporting interval.

### disk.md.d_avg_rqsz

average I/O request size for discards to the per-multi-device logical device
during the reporting interval.

### disk.md.util

The percentage of time during the reporting interval that the
per-multi-device logical device was busy processing requests
(reads and writes). A value of 100% indicates device saturation.
## filesys

### filesys.capacity

Total capacity of mounted filesystem (Kbytes)

### filesys.used

Total space used on mounted filesystem (Kbytes)

### filesys.free

Total space free on mounted filesystem (Kbytes)

### filesys.maxfiles

Inodes capacity of mounted filesystem

### filesys.usedfiles

Number of inodes allocated on mounted filesystem

### filesys.freefiles

Number of unallocated inodes on mounted filesystem

### filesys.mountdir

File system mount point

### filesys.full

Percentage of filesystem in use

### filesys.blocksize

Size of each block on mounted filesystem (Bytes)

### filesys.avail

Total space free to non-superusers on mounted filesystem (Kbytes)

### filesys.readonly

Indicates whether a filesystem is mounted readonly
## swap

### swap.pagesin

pages read from swap devices due to demand for physical memory

### swap.pagesout

pages written to swap devices due to demand for physical memory

### swap.in

number of swap in operations

### swap.out

number of swap out operations

### swap.free

swap free metric from /proc/meminfo

### swap.length

total swap available metric from /proc/meminfo

### swap.used

swap used metric from /proc/meminfo
## mem

### mem.physmem

The value of this metric corresponds to the "MemTotal" field
reported by /proc/meminfo. Note that this does not necessarily
correspond to actual installed physical memory - there may
be areas of the physical address space mapped as ROM in
various peripheral devices and the bios may be mirroring
certain ROMs in RAM.

### mem.freemem

free system memory metric from /proc/meminfo

### mem.util.used

Used memory is the difference between mem.physmem and mem.freemem.

### mem.util.free

Alias for mem.freemem.

### mem.util.shared

Shared memory metric. Currently always zero on Linux 2.4 kernels
and has been removed from 2.6 kernels.

### mem.util.bufmem

Memory allocated for buffer_heads.

### mem.util.cached

Memory used by the page cache, including buffered file data.
This is in-memory cache for files read from the disk (the pagecache)
but doesn't include SwapCached.

### mem.util.other

Memory that is not free (i.e. has been referenced) and is not cached.
mem.physmem - mem.util.free - mem.util.cached - mem.util.buffers

### mem.util.swapCached

Memory that once was swapped out, is swapped back in but still also
is in the swapfile (if memory is needed it doesn't need to be swapped
out AGAIN because it is already in the swapfile. This saves I/O)

### mem.util.active

Memory that has been used more recently and usually not reclaimed unless
absolutely necessary.

### mem.util.inactive

Memory which has been less recently used.  It is more eligible to be
reclaimed for other purposes

### mem.util.highTotal

This is apparently an i386 specific metric, and seems to be always zero
on ia64 architecture (and possibly others). On i386 arch (at least),
highmem is all memory above ~860MB of physical memory. Highmem areas
are for use by userspace programs, or for the pagecache. The kernel
must use tricks to access this memory, making it slower to access
than lowmem.

### mem.util.highFree

See mem.util.highTotal. Not used on ia64 arch (and possibly others).

### mem.util.lowTotal

Lowmem is memory which can be used for everything that highmem can be
used for, but it is also availble for the kernel's use for its own
data structures. Among many other things, it is where everything
from the Slab is allocated.  Bad things happen when you're out of lowmem.
(this may only be true on i386 architectures).

### mem.util.lowFree

See mem.util.lowTotal

### mem.util.swapTotal

total amount of swap space available

### mem.util.swapFree

Memory which has been evicted from RAM, and is temporarily on the disk

### mem.util.dirty

Memory which is waiting to get written back to the disk

### mem.util.writeback

Memory which is actively being written back to the disk

### mem.util.mapped

files which have been mmaped, such as libraries

### mem.util.slab

in-kernel data structures cache

### mem.util.committed_AS

An estimate of how much RAM you would need to make a 99.99% guarantee
that there never is OOM (out of memory) for this workload. Normally
the kernel will overcommit memory. That means, say you do a 1GB malloc,
nothing happens, really. Only when you start USING that malloc memory
you will get real memory on demand, and just as much as you use.

### mem.util.pageTables

Kbytes in kernel page tables, from /proc/meminfo

### mem.util.reverseMaps

Kbytes in reverse mapped pages, from /proc/meminfo

### mem.util.cache_clean

Kbytes cached and not dirty or writeback, derived from /proc/meminfo

### mem.util.anonpages

Kbytes in user pages not backed by files, from /proc/meminfo

### mem.util.commitLimit

The static total, in Kbytes, available for commitment to address
spaces. Thus, mem.util.committed_AS may range up to this total. Normally
the kernel overcommits memory, so this value may exceed mem.physmem

### mem.util.bounce

Kbytes in bounce buffers, from /proc/meminfo

### mem.util.NFS_Unstable

Kbytes in NFS unstable memory, from /proc/meminfo

### mem.util.slabReclaimable

Kbytes in reclaimable slab pages, from /proc/meminfo

### mem.util.slabUnreclaimable

Kbytes in unreclaimable slab pages, from /proc/meminfo

### mem.util.active_anon

anonymous Active list LRU memory

### mem.util.inactive_anon

anonymous Inactive list LRU memory

### mem.util.active_file

file-backed Active list LRU memory

### mem.util.inactive_file

file-backed Inactive list LRU memory

### mem.util.unevictable

kbytes of memory that is unevictable

### mem.util.mlocked

kbytes of memory that is pinned via mlock()

### mem.util.shmem

kbytes of shmem

### mem.util.kernelStack

kbytes of memory used for kernel stacks

### mem.util.hugepagesTotal

a count of total hugepages

### mem.util.hugepagesFree

a count of free hugepages

### mem.util.hugepagesRsvd

a count of reserved hugepages

### mem.util.hugepagesSurp

a count of surplus hugepages

### mem.util.directMap4k

amount of memory that is directly mapped in 4kB pages

### mem.util.directMap2M

amount of memory that is directly mapped in 2MB pages

### mem.util.vmallocTotal

amount of kernel memory allocated via vmalloc

### mem.util.vmallocUsed

amount of used vmalloc memory

### mem.util.vmallocChunk

amount of vmalloc chunk memory

### mem.util.mmap_copy

amount of mmap_copy space (non-MMU kernels only)

### mem.util.quicklists

amount of memory in the per-CPU quicklists

### mem.util.corrupthardware

amount of memory in hardware corrupted pages

### mem.util.anonhugepages

amount of memory in anonymous huge pages

### mem.util.directMap1G

amount of memory that is directly mapped in 1GB pages

### mem.util.available

The amount of memory that is available for a new workload,
without pushing the system into swap. Estimated from MemFree,
Active(file), Inactive(file), and SReclaimable, as well as the "low"
watermarks from /proc/zoneinfo.

### mem.util.hugepagesTotalBytes

amount of memory in total hugepages

### mem.util.hugepagesFreeBytes

amount of memory in free hugepages

### mem.util.hugepagesRsvdBytes

amount of memory in reserved hugepages

### mem.util.hugepagesSurpBytes


User memory (Kbytes) in pages not backed by files, e.g. from malloc()

### mem.numa.max_bandwidth

Maximum memory bandwidth supported on each numa node. It makes use of a
bandwith.conf file which has the bandwidth information for each node :
node_num:bandwidth
The node_num must match with any node in sysfs/devices/system/node directory.
And, the bandwidth is expressed in terms of MBps. This config file should be
filled up manually after running some bandwidth saturation benchmark tools.

### mem.numa.util.total

per-node total memory

### mem.numa.util.free

per-node free memory

### mem.numa.util.used

per-node used memory

### mem.numa.util.active

per-node Active list LRU memory

### mem.numa.util.inactive

per-node Inactive list LRU memory

### mem.numa.util.active_anon

per-node anonymous Active list LRU memory

### mem.numa.util.inactive_anon

per-node anonymous Inactive list LRU memory

### mem.numa.util.active_file

per-node file-backed Active list LRU memory

### mem.numa.util.inactive_file

per-node file-backed Inactive list LRU memory

### mem.numa.util.highTotal

per-node highmem total

### mem.numa.util.highFree

per-node highmem free

### mem.numa.util.lowTotal

per-node lowmem total

### mem.numa.util.lowFree

per-node lowmem free

### mem.numa.util.unevictable

per-node Unevictable memory

### mem.numa.util.mlocked

per-node count of Mlocked memory

### mem.numa.util.dirty

per-node dirty memory

### mem.numa.util.writeback

per-node count of memory locked for writeback to stable storage

### mem.numa.util.filePages

per-node count of memory backed by files

### mem.numa.util.mapped

per-node mapped memory

### mem.numa.util.anonpages

per-node anonymous memory

### mem.numa.util.shmem

per-node amount of shared memory

### mem.numa.util.kernelStack

per-node memory used as kernel stacks

### mem.numa.util.pageTables

per-node memory used for pagetables

### mem.numa.util.NFS_Unstable

per-node memory holding NFS data that needs writeback

### mem.numa.util.bounce

per-node memory used for bounce buffers

### mem.numa.util.writebackTmp

per-node temporary memory used for writeback

### mem.numa.util.slab

per-node memory used for slab objects

### mem.numa.util.slabReclaimable

per-node memory used for slab objects that can be reclaimed

### mem.numa.util.slabUnreclaimable

per-node memory used for slab objects that is unreclaimable

### mem.numa.util.hugepagesTotal

per-node total count of hugepages

### mem.numa.util.hugepagesFree

per-node count of free hugepages

### mem.numa.util.hugepagesSurp

per-node count of surplus hugepages

### mem.numa.util.hugepagesTotalBytes

per-node total amount of hugepages memory

### mem.numa.util.hugepagesFreeBytes

per-node amount of free hugepages memory

### mem.numa.util.hugepagesSurpBytes

per-node amount of surplus hugepages memory

### mem.numa.alloc.hit

per-node count of times a task wanted alloc on local node and succeeded

### mem.numa.alloc.miss

per-node count of times a task wanted alloc on local node but got another node

### mem.numa.alloc.foreign

count of times a task on another node alloced on that node, but got this node

### mem.numa.alloc.interleave_hit

count of times interleaving wanted to allocate on this node and succeeded

### mem.numa.alloc.local_node

count of times a process ran on this node and got memory on this node

### mem.numa.alloc.other_node

count of times a process ran on this node and got memory from another node

### mem.vmstat.allocstall

Count of direct reclaim calls since boot, from /proc/vmstat

### mem.vmstat.allocstall_dma

Count of direct dma reclaim calls since boot, from /proc/vmstat

### mem.vmstat.allocstall_dma32

Count of direct dma32 reclaim calls since boot, from /proc/vmstat

### mem.vmstat.allocstall_high

Count of direct high mem reclaim calls since boot, from /proc/vmstat

### mem.vmstat.allocstall_movable

Count of direct movable mem reclaim calls since boot, from /proc/vmstat

### mem.vmstat.allocstall_normal

Count of direct normal mem reclaim calls since boot, from /proc/vmstat

### mem.vmstat.balloon_deflate

number of virt guest balloon page deflations

### mem.vmstat.balloon_inflate

count of virt guest balloon page inflations

### mem.vmstat.balloon_migrate

number of virt guest balloon page migrations

### mem.vmstat.compact_blocks_moved

count of compact blocks moved

### mem.vmstat.compact_daemon_free_scanned

count of pages scanned for migration by compaction daemon

### mem.vmstat.compact_daemon_migrate_scanned

count of pages scanned for migration by compaction daemon

### mem.vmstat.compact_daemon_wake

number of times the memory compaction daemon was woken

### mem.vmstat.compact_fail

count of unsuccessful compactions for high order allocations

### mem.vmstat.compact_free_scanned

count of pages scanned for freeing

### mem.vmstat.compact_isolated

count of isolated compaction pages

### mem.vmstat.compact_migrate_scanned

count of pages scanned for migration

### mem.vmstat.compact_pagemigrate_failed

count of pages unsuccessfully compacted

### mem.vmstat.compact_pages_moved

count of pages successfully moved for compaction

### mem.vmstat.compact_stall

count of failures to even start compacting

### mem.vmstat.compact_success

count of successful compactions for high order allocations

### mem.vmstat.drop_pagecache

count of calls to drop page cache pages

### mem.vmstat.drop_slab

count of calls to drop slab cache pages

### mem.vmstat.htlb_buddy_alloc_fail

Count of huge TLB page buddy allocation failures, from /proc/vmstat

### mem.vmstat.htlb_buddy_alloc_success

Count of huge TLB page buddy allocation successes, from /proc/vmstat

### mem.vmstat.kswapd_inodesteal

Count of pages reclaimed via kswapd inode freeing since boot, from
/proc/vmstat

### mem.vmstat.kswapd_low_wmark_hit_quickly

Count of times kswapd reached low watermark quickly, from /proc/vmstat

### mem.vmstat.kswapd_high_wmark_hit_quickly

Count of times kswapd reached high watermark quickly, from /proc/vmstat

### mem.vmstat.kswapd_skip_congestion_wait

Count of times kswapd skipped waiting due to device congestion as a
result of being under the low watermark, from /proc/vmstat

### mem.vmstat.kswapd_steal

Count of pages reclaimed by kswapd since boot, from /proc/vmstat

### mem.vmstat.nr_active_anon

number of active anonymous memory pages

### mem.vmstat.nr_active_file

number of active file memory memory pages

### mem.vmstat.nr_anon_pages

Instantaneous number of anonymous mapped pagecache pages, from /proc/vmstat
See also mem.vmstat.mapped for other mapped pages.

### mem.vmstat.nr_anon_transparent_hugepages

Instantaneous number of anonymous transparent huge pages, from /proc/vmstat

### mem.vmstat.nr_bounce

Instantaneous number of bounce buffer pages, from /proc/vmstat

### mem.vmstat.nr_dirtied

Count of pages entering dirty state, from /proc/vmstat

### mem.vmstat.nr_dirty

Instantaneous number of pages in dirty state, from /proc/vmstat

### mem.vmstat.nr_dirty_background_threshold

background writeback threshold

### mem.vmstat.nr_dirty_threshold

dirty throttling threshold

### mem.vmstat.nr_file_hugepages

count of hugepages used for files

### mem.vmstat.nr_file_pages

count of pages used for files

### mem.vmstat.nr_file_pmdmapped

count of PMD mappings used for files

### mem.vmstat.nr_foll_pin_acquired

count of pinned user memory acquisitions

### mem.vmstat.nr_foll_pin_released

count of pinned user memory releases

### mem.vmstat.nr_free_cma

count of free Contiguous Memory Allocator pages

### mem.vmstat.nr_free_pages

number of free pages

### mem.vmstat.nr_inactive_anon

number of inactive anonymous memory pages

### mem.vmstat.nr_inactive_file

number of inactive file memory pages

### mem.vmstat.nr_isolated_anon

number of isolated anonymous memory pages

### mem.vmstat.nr_isolated_file

number of isolated file memory pages

### mem.vmstat.nr_kernel_misc_reclaimable

number of misc reclaimable kernel pages

### mem.vmstat.nr_kernel_stack

number of pages of kernel stack

### mem.vmstat.nr_mapped

Instantaneous number of mapped pagecache pages, from /proc/vmstat
See also mem.vmstat.nr_anon for anonymous mapped pages.

### mem.vmstat.nr_mlock

number of pages under mlock

### mem.vmstat.nr_pages_scanned

count of pages scanned during page reclaim

### mem.vmstat.nr_page_table_pages

Instantaneous number of page table pages, from /proc/vmstat

### mem.vmstat.nr_shmem

number of shared memory pages

### mem.vmstat.nr_shmem_hugepages

number of huge pages used for shared memory

### mem.vmstat.nr_shmem_pmdmapped

number of PMD mappings used for shared memory

### mem.vmstat.nr_slab

Instantaneous number of slab pages, from /proc/vmstat
This counter was retired in 2.6.18 kernels, and is now the sum of
mem.vmstat.nr_slab_reclaimable and mem.vmstat.nr_slab_unreclaimable.

### mem.vmstat.nr_slab_reclaimable

Instantaneous number of reclaimable slab pages, from /proc/vmstat.

### mem.vmstat.nr_slab_unreclaimable

Instantaneous number of unreclaimable slab pages, from /proc/vmstat.

### mem.vmstat.nr_unevictable

number of unevictable pages

### mem.vmstat.nr_unstable

Instantaneous number of pages in unstable state, from /proc/vmstat

### mem.vmstat.nr_vmscan_immediate_reclaim

prioritise for reclaim when writeback ends

### mem.vmstat.nr_vmscan_write

Count of pages written from the LRU by the VM scanner, from /proc/vmstat.
The VM is supposed to minimise the number of pages which get written
from the LRU (for IO scheduling efficiency, and for high reclaim-success
rates).

### mem.vmstat.nr_writeback

Instantaneous number of pages in writeback state, from /proc/vmstat

### mem.vmstat.nr_writeback_temp

number of temporary writeback pages

### mem.vmstat.nr_written

Count of pages written out, from /proc/vmstat

### mem.vmstat.nr_zone_active_anon

number of inactive file memory pages in zones

### mem.vmstat.nr_zone_active_file

number of isolated file memory pages in zones

### mem.vmstat.nr_zone_inactive_anon

number of inactive anonymous memory pages in zones

### mem.vmstat.nr_zone_inactive_file

number of isolated anonymous memory pages in zones

### mem.vmstat.nr_zone_unevictable

number of unevictable memory pages in zones

### mem.vmstat.nr_zone_write_pending

count of dirty, writeback and unstable pages

### mem.vmstat.nr_zspages

number of compressed pages

### mem.vmstat.numa_foreign

count of foreign NUMA zone allocations

### mem.vmstat.numa_hint_faults

count of page migrations from NUMA PTE fault hints

### mem.vmstat.numa_hint_faults_local

count of NUMA PTE fault hints satisfied locally

### mem.vmstat.numa_hit

count of successful allocations from preferred NUMA zone

### mem.vmstat.numa_huge_pte_updates

count of NUMA huge page table entry updates

### mem.vmstat.numa_interleave

count of interleaved NUMA allocations

### mem.vmstat.numa_local

count of successful allocations from local NUMA zone

### mem.vmstat.numa_miss

count of unsuccessful allocations from preferred NUMA zona

### mem.vmstat.numa_other

count of unsuccessful allocations from local NUMA zone

### mem.vmstat.numa_pages_migrated

count of NUMA page migrations

### mem.vmstat.numa_pte_updates

count of NUMA page table entry updates

### mem.vmstat.oom_kill

count of out-of-memory kills

### mem.vmstat.pageoutrun

Count of kswapd calls to page reclaim since boot, from /proc/vmstat

### mem.vmstat.pgactivate

Count of pages moved from inactive to active since boot, from /proc/vmstat

### mem.vmstat.pgalloc_dma

Count of dma mem page allocations since boot, from /proc/vmstat

### mem.vmstat.pgalloc_dma32

Count of dma32 mem page allocations since boot, from /proc/vmstat

### mem.vmstat.pgalloc_high

Count of high mem page allocations since boot, from /proc/vmstat

### mem.vmstat.pgalloc_movable

Count of movable mem page allocations since boot, from /proc/vmstat

### mem.vmstat.pgalloc_normal

Count of normal mem page allocations since boot, from /proc/vmstat

### mem.vmstat.pgrefill_dma32

Count of dma32 mem pages inspected in refill_inactive_zone since boot,
from /proc/vmstat

### mem.vmstat.pgrefill_movable

Count of movable mem pages inspected in refill_inactive_zone since boot,
from /proc/vmstat

### mem.vmstat.pgdeactivate

Count of pages moved from active to inactive since boot, from /proc/vmstat

### mem.vmstat.pgfault

Count of page major and minor fault operations since boot, from /proc/vmstat

### mem.vmstat.pgfree

Count of page free operations since boot, from /proc/vmstat

### mem.vmstat.pginodesteal

Count of pages reclaimed via inode freeing since boot, from /proc/vmstat

### mem.vmstat.pglazyfreed

count of pages lazily freed

### mem.vmstat.pgmajfault

Count of major page fault operations since boot, from /proc/vmstat

### mem.vmstat.pgmigrate_fail

count of unsuccessful NUMA page migrations

### mem.vmstat.pgmigrate_success

count of successful NUMA page migrations

### mem.vmstat.pgpgin

Count of page in operations since boot, from /proc/vmstat

### mem.vmstat.pgpgout

Count of page out operations since boot, from /proc/vmstat

### mem.vmstat.pgrefill_dma

Count of dma mem pages inspected in refill_inactive_zone since boot,
from /proc/vmstat

### mem.vmstat.pgrefill_high

Count of high mem pages inspected in refill_inactive_zone since boot,
from /proc/vmstat

### mem.vmstat.pgrefill_normal

Count of normal mem pages inspected in refill_inactive_zone since boot,
from /proc/vmstat

### mem.vmstat.pgrotated

Count of pages rotated to tail of the LRU since boot, from /proc/vmstat

### mem.vmstat.pgscan_direct

Count of mem pages scanned directly since boot, from /proc/vmstat
since Linux 3.4

### mem.vmstat.pgscan_direct_dma

Count of dma mem pages scanned since boot, from /proc/vmstat

### mem.vmstat.pgscan_direct_dma32

Count of dma32 mem pages scanned since boot, from /proc/vmstat

### mem.vmstat.pgscan_direct_high

Count of high mem pages scanned since boot, from /proc/vmstat

### mem.vmstat.pgscan_direct_movable

Count of movable mem pages scanned since boot, from /proc/vmstat

### mem.vmstat.pgscan_direct_normal

Count of normal mem pages scanned since boot, from /proc/vmstat

### mem.vmstat.pgscan_direct_throttle

Count of throttled mem pages scanned directly since boot, from /proc/vmstat
since Linux 3.4

### mem.vmstat.pgscan_direct_total

cumulative total of directly scanned mem pages

### mem.vmstat.pgscan_kswapd

Count of mem pages scanned by kswapd since boot, from /proc/vmstat
since Linux 3.4

### mem.vmstat.pgscan_kswapd_dma

Count of dma mem pages scanned by kswapd since boot, from /proc/vmstat

### mem.vmstat.pgscan_kswapd_dma32

Count of dma32 mem pages scanned by kswapd since boot, from /proc/vmstat

### mem.vmstat.pgscan_kswapd_high

Count of high mem pages scanned by kswapd since boot, from /proc/vmstat

### mem.vmstat.pgscan_kswapd_movable

Count of movable mem pages scanned by kswapd since boot, from /proc/vmstat

### mem.vmstat.pgscan_kswapd_normal

Count of normal mem pages scanned by kswapd since boot, from /proc/vmstat

### mem.vmstat.pgscan_kswapd_total

cumulative total mem pages scanned by kswapd

### mem.vmstat.pgsteal_dma

Count of dma mem pages reclaimed since boot, from /proc/vmstat

### mem.vmstat.pgsteal_dma32

Count of dma32 mem pages reclaimed since boot, from /proc/vmstat

### mem.vmstat.pgsteal_file

Count of file memory pages reclaimed since boot, from /proc/vmstat

### mem.vmstat.pgsteal_high

Count of high mem pages reclaimed since boot, from /proc/vmstat

### mem.vmstat.pgsteal_movable

Count of movable mem pages reclaimed since boot, from /proc/vmstat

### mem.vmstat.pgsteal_normal

Count of normal mem pages reclaimed since boot, from /proc/vmstat

### mem.vmstat.pgsteal_kswapd

Count of mem pages reclaimed by kswapd since boot, from /proc/vmstat

### mem.vmstat.pgsteal_kswapd_dma

Count of dma mem pages reclaimed by kswapd since boot, from /proc/vmstat
since Linux 3.4

### mem.vmstat.pgsteal_kswapd_dma32

Count of dma32 mem pages reclaimed by kswapd since boot, from /proc/vmstat
since Linux 3.4

### mem.vmstat.pgsteal_kswapd_normal

Count of normal mem pages reclaimed by kswapd since boot, from /proc/vmstat
since Linux 3.4

### mem.vmstat.pgsteal_kswapd_movable

Count of movable mem pages reclaimed by kswapd since boot, from /proc/vmstat
since Linux 3.4

### mem.vmstat.pgsteal_direct

Count of mem pages directly reclaimed since boot, from /proc/vmstat

### mem.vmstat.pgsteal_direct_dma

Count of dma mem pages reclaimed since boot, from /proc/vmstat
since Linux 3.4

### mem.vmstat.pgsteal_direct_dma32

Count of dma32 mem pages reclaimed since boot, from /proc/vmstat
since Linux 3.4

### mem.vmstat.pgsteal_direct_normal

Count of normal mem pages reclaimed since boot, from /proc/vmstat
since Linux 3.4

### mem.vmstat.pgsteal_direct_movable

Count of movable mem pages reclaimed since boot, from /proc/vmstat
since Linux 2.6.23

### mem.vmstat.pgsteal_total

cumulative total mem pages reclaimed

### mem.vmstat.pswpin

Count of pages swapped in since boot, from /proc/vmstat

### mem.vmstat.pswpout

Count of pages swapped out since boot, from /proc/vmstat

### mem.vmstat.slabs_scanned

Count of slab pages scanned since boot, from /proc/vmstat

### mem.vmstat.swap_ra

count of swap pages readahead

### mem.vmstat.swap_ra_hit

count of swap pages readahead that were used

### mem.vmstat.thp_collapse_alloc

transparent huge page collapse allocations

### mem.vmstat.thp_collapse_alloc_failed

transparent huge page collapse failures

### mem.vmstat.thp_deferred_split_page

count of huge page enqueues for splitting

### mem.vmstat.thp_fault_alloc

transparent huge page fault allocations

### mem.vmstat.thp_fault_fallback

transparent huge page fault fallbacks

### mem.vmstat.thp_fault_fallback_charge

transparent huge page fault fallback charges

### mem.vmstat.thp_file_alloc

transparent huge page file allocations

### mem.vmstat.thp_file_mapped

transparent huge page file mappings

### mem.vmstat.thp_split

count of transparent huge page splits

### mem.vmstat.thp_split_page

count of huge page splits into base pages

### mem.vmstat.thp_split_page_failed

count of failures to split a huge page

### mem.vmstat.thp_split_pmd

This can happen, for instance, when an application calls mprotect() or
munmap() on part of huge page. It doesn't split the huge page, only the
page table entry.

### mem.vmstat.thp_split_pud

count of times a huge page PUD was split

### mem.vmstat.thp_swpout

count of transparent huge page swapouts

### mem.vmstat.thp_swpout_fallback

count of transparent huge page swapout fallbacks

### mem.vmstat.thp_zero_page_alloc

count of transparent huge page zeroed page allocations

### mem.vmstat.thp_zero_page_alloc_failed

count of transparent huge page zeroed page allocation failures

### mem.vmstat.unevictable_pgs_cleared

count of unevictable pages cleared

### mem.vmstat.unevictable_pgs_culled

count of unevictable pages culled

### mem.vmstat.unevictable_pgs_mlocked

count of mlocked unevictable pages

### mem.vmstat.unevictable_pgs_mlockfreed

count of unevictable pages mlock freed

### mem.vmstat.unevictable_pgs_munlocked

count of unevictable pages munlocked

### mem.vmstat.unevictable_pgs_rescued

count of unevictable pages rescued

### mem.vmstat.unevictable_pgs_scanned

count of unevictable pages scanned

### mem.vmstat.unevictable_pgs_stranded

count of unevictable pages stranded

### mem.vmstat.workingset_activate

count of page activations to form the working set

### mem.vmstat.workingset_nodes

count of NUMA nodes holding the working set

### mem.vmstat.workingset_nodereclaim

count of NUMA node working set page reclaims

### mem.vmstat.workingset_refault

count of refaults of previously evicted pages

### mem.vmstat.workingset_restore

count of restored of previously evicted pages

### mem.vmstat.zone_reclaim_failed

number of zone reclaim failures

### mem.buddyinfo.pages

fragmented page count from /proc/buddyinfo

### mem.buddyinfo.total

page fragmentation size from /proc/buddyinfo

### mem.slabinfo.objects.active

number of active objects in each cache

### mem.slabinfo.objects.total

total number of objects in each cache

### mem.slabinfo.objects.size

size of individual objects of each cache

### mem.slabinfo.slabs.active

number of active slabs comprising each cache

### mem.slabinfo.slabs.total

total number of slabs comprising each cache

### mem.slabinfo.slabs.pages_per_slab

number of pages in each slab

### mem.slabinfo.slabs.objects_per_slab

number of objects in each slab

### mem.slabinfo.slabs.total_size

total number of bytes allocated for active objects in each slab

### mem.zoneinfo.free

free space in each zone for each NUMA node

### mem.zoneinfo.min

min space in each zone for each NUMA node

### mem.zoneinfo.low

low space in each zone for each NUMA node

### mem.zoneinfo.high

high space in each zone for each NUMA node

### mem.zoneinfo.scanned

scanned space in each zone for each NUMA node

### mem.zoneinfo.spanned

spanned space in each zone for each NUMA node

### mem.zoneinfo.present

present space in each zone for each NUMA node

### mem.zoneinfo.managed

managed space in each zone for each NUMA node

### mem.zoneinfo.nr_free_pages

number of free pages in each zone for each NUMA node.

### mem.zoneinfo.nr_alloc_batch

Number of pages allocated to other zones due to insufficient memory, for
each zone for each NUMA node.

### mem.zoneinfo.nr_inactive_anon

number of inactive anonymous memory pages in each zone for each NUMA node

### mem.zoneinfo.nr_active_anon

number of active anonymous memory pages in each zone for each NUMA node

### mem.zoneinfo.nr_inactive_file

number of inactive file memory pages in each zone for each NUMA node

### mem.zoneinfo.nr_active_file

number of active file memory memory pages in each zone for each NUMA node

### mem.zoneinfo.nr_unevictable

number of unevictable pages in each zone for each NUMA node

### mem.zoneinfo.nr_mlock

number of pages under mlock in each zone for each NUMA node

### mem.zoneinfo.nr_anon_pages

number of anonymous mapped pagecache pages in each zone for each NUMA node

### mem.zoneinfo.nr_mapped

number of mapped pagecache pages in each zone for each NUMA node

### mem.zoneinfo.nr_file_pages

number of file pagecache pages in each zone for each NUMA node

### mem.zoneinfo.nr_dirty

number of pages dirty state in each zone for each NUMA node

### mem.zoneinfo.nr_writeback

number of pages writeback state in each zone for each NUMA node

### mem.zoneinfo.nr_slab_reclaimable

number of reclaimable slab pages in each zone for each NUMA node

### mem.zoneinfo.nr_slab_unreclaimable

number of unreclaimable slab pages in each zone for each NUMA node

### mem.zoneinfo.nr_page_table_pages

number of page table pages in each zone for each NUMA node

### mem.zoneinfo.nr_kernel_stack

number of pages of kernel stack in each zone for each NUMA node

### mem.zoneinfo.nr_unstable

number of pages unstable state in each zone for each NUMA node

### mem.zoneinfo.nr_bounce

number of bounce buffer pages in each zone for each NUMA node

### mem.zoneinfo.nr_vmscan_write

Count of pages written from the LRU by the VM scanner in each zone
for each NUMA node.The VM is supposed to minimise the number of
pages which get written from the LRU (for IO scheduling efficiency,
and for high reclaim-success rates).

### mem.zoneinfo.nr_vmscan_immediate_reclaim

prioritise for reclaim when writeback ends in each zone for each NUMA node

### mem.zoneinfo.nr_writeback_temp

number of temporary writeback pages in each zone for each NUMA node

### mem.zoneinfo.nr_isolated_anon

number of isolated anonymous memory pages in each zone for each NUMA node

### mem.zoneinfo.nr_isolated_file

number of isolated file memory pages in each zone for each NUMA node

### mem.zoneinfo.nr_shmem

number of shared memory pages in each zone for each NUMA node

### mem.zoneinfo.nr_dirtied

count of pages entering dirty state in each zone for each NUMA node

### mem.zoneinfo.nr_written

count of pages written out in each zone for each NUMA node

### mem.zoneinfo.numa_hit

Count of successful allocations from preferred NUMA zone in each zone
for each NUMA node.

### mem.zoneinfo.numa_miss

Count of unsuccessful allocations from preferred NUMA zone in each zone
for each NUMA node.

### mem.zoneinfo.numa_foreign

Count of foreign NUMA zone allocations in each zone for each NUMA node.

### mem.zoneinfo.numa_interleave

count of interleaved NUMA allocations in each zone for each NUMA node

### mem.zoneinfo.numa_local

Count of successful allocations from local NUMA zone in each zone for
each NUMA node.

### mem.zoneinfo.numa_other

Count of unsuccessful allocations from local NUMA zone in each zone for
each NUMA node.

### mem.zoneinfo.workingset_refault

count of refaults of previously evicted pages in each zone for each NUMA node

### mem.zoneinfo.workingset_activate

count of page activations to form the working set in each zone for each NUMA node

### mem.zoneinfo.workingset_nodereclaim

count of NUMA node working set page reclaims in each zone for each NUMA node

### mem.zoneinfo.nr_anon_transparent_hugepages

number of anonymous transparent huge pages in each zone for each NUMA node

### mem.zoneinfo.nr_free_cma

count of free Contiguous Memory Allocator pages in each zone for each NUMA node.

### mem.zoneinfo.protection

protection space in each zone for each NUMA node

### mem.ksm.full_scans

Number of times that KSM has scanned for duplicated content

### mem.ksm.merge_across_nodes

Kernel allows merging across NUMA nodes

### mem.ksm.pages_shared

The number of nodes in the stable tree

### mem.ksm.pages_sharing

The number of virtual pages that are sharing a single page

### mem.ksm.pages_to_scan

Number of pages to scan at a time

### mem.ksm.pages_unshared

The number of nodes in the unstable tree

### mem.ksm.pages_volatile

Number of pages that are candidate to be shared

### mem.ksm.run_state

Whether the KSM daemon has run and/or is running

### mem.ksm.sleep_time

Time ksmd should sleep between batches
## network

### network.all.in.bytes

Sum of bytes column on the "Receive" side of /proc/net/dev for network
interfaces deemed to be 'physical' interfaces, using regular expression
pattern described in the $PCP_SYSCONF_DIR/linux/interfaces.conf file.

### network.all.in.packets

Sum of packets column on the "Receive" side of /proc/net/dev for network
interfaces deemed to be 'physical' interfaces, using regular expression
pattern described in the $PCP_SYSCONF_DIR/linux/interfaces.conf file.

### network.all.in.errors

Sum of errors column on the "Receive" side of /proc/net/dev for network
interfaces deemed to be 'physical' interfaces, using regular expression
pattern described in the $PCP_SYSCONF_DIR/linux/interfaces.conf file.

### network.all.in.drops

Sum of drop column on the "Receive" side of /proc/net/dev for network
interfaces deemed to be 'physical' interfaces, using regular expression
pattern described in the $PCP_SYSCONF_DIR/linux/interfaces.conf file.

### network.all.out.bytes

Sum of bytes column on the "Transmit" side of /proc/net/dev for network
interfaces deemed to be 'physical' interfaces, using regular expression
pattern described in the $PCP_SYSCONF_DIR/linux/interfaces.conf file.

### network.all.out.packets

Sum of packets column on the "Transmit" side of /proc/net/dev for network
interfaces deemed to be 'physical' interfaces, using regular expression
pattern described in the $PCP_SYSCONF_DIR/linux/interfaces.conf file.

### network.all.out.errors

Sum of errors column on the "Transmit" side of /proc/net/dev for network
interfaces deemed to be 'physical' interfaces, using regular expression
pattern described in the $PCP_SYSCONF_DIR/linux/interfaces.conf file.

### network.all.out.drops

Sum of drop column on the "Transmit" side of /proc/net/dev for network
interfaces deemed to be 'physical' interfaces, using regular expression
pattern described in the $PCP_SYSCONF_DIR/linux/interfaces.conf file.

### network.all.total.bytes

Sum of network.all.in.bytes and network.all.out.bytes metrics.

### network.all.total.packets

Sum of network.all.in.packets and network.all.out.packets metrics.

### network.all.total.errors

Sum of network.all.in.errors and network.all.out.errors metrics.

### network.all.total.drops

Sum of network.all.in.drops and network.all.out.drops metrics.

### network.interface.collisions

colls column on the "Transmit" side of /proc/net/dev
(stats->collisions counter in rtnl_link_stats64).
Counter only valid for outgoing packets.

### network.interface.mtu

maximum transmission unit on network interface

### network.interface.speed

The linespeed on the network interface, as reported by the kernel,
scaled from Megabits/second to Megabytes/second.
See also network.interface.baudrate for the bytes/second value.

### network.interface.baudrate

The linespeed on the network interface, as reported by the kernel,
scaled up from Megabits/second to bits/second and divided by 8 to convert
to bytes/second.
See also network.interface.speed for the Megabytes/second value.

### network.interface.duplex

value one for half or two for full duplex interface

### network.interface.up

boolean for whether interface is currently up or down

### network.interface.running

boolean for whether interface has resources allocated

### network.interface.wireless

boolean for whether interface is wireless

### network.interface.type

sysfs interface name assignment type value

### network.interface.inet_addr

string INET interface address (ifconfig style)

### network.interface.ipv6_addr

string IPv6 interface address (ifconfig style)

### network.interface.ipv6_scope

string IPv6 interface scope (ifconfig style)

### network.interface.hw_addr

hardware address (from sysfs)

### network.interface.in.bytes

bytes column on the "Receive" side of /proc/net/dev (stats->rx_bytes counter in
rtnl_link_stats64)

### network.interface.in.packets

packets column on the "Receive" side of /proc/net/dev
(stats->rx_packets counter in rtnl_link_stats64)

### network.interface.in.errors

errors column on the "Receive" side of /proc/net/dev
(stats->rx_errors counter in rtnl_link_stats64)

### network.interface.in.drops

drop column on the "Receive" side of /proc/net/dev
(stats->{rx_dropped + rx_missed_errors} counters in rtnl_link_stats64)
rx_dropped are the dropped packets due to no space in linux buffers and rx_missed
are due to the receiver NIC missing a packet.
Not all NICS use the rx_missed_errors counter.

### network.interface.in.fifo

fifo column on the "Receive" side of /proc/net/dev
(stats->rx_fifo_errors counter in rtnl_link_stats64)

### network.interface.in.frame

frame column on the "Receive" side of /proc/net/dev
(stats->{rx_length_errors + rx_over_errors + rx_crc_errors + rx_frame_errors}
counters in rtnl_link_stats64)

### network.interface.in.compressed

compressed column on the "Receive" side of /proc/net/dev
(stats->rx_compressed counter in rtnl_link_stats64).
Almost exclusively used for CSLIP or HDLC devices

### network.interface.in.mcasts

multicast column on the "Receive" side of /proc/net/dev
(stats->multicast counter in rtnl_link_stats64)

### network.interface.out.bytes

bytes column on the "Transmit" side of /proc/net/dev
(stats->tx_bytes counter in rtnl_link_stats64)

### network.interface.out.packets

packets column on the "Transmit" side of /proc/net/dev
(stats->tx_packets counter in rtnl_link_stats64)

### network.interface.out.errors

errors column on the "Transmit" side of /proc/net/dev
(stats->tx_errors counter in rtnl_link_stats64)

### network.interface.out.drops

drop column on the "Transmit" side of /proc/net/dev
(stats->tx_dropped counter in rtnl_link_stats64)

### network.interface.out.fifo

fifo column on the "Transmit" side of /proc/net/dev
(stats->tx_fifo_errors counter in rtnl_link_stats64)

### network.interface.out.carrier

carrier column on the "Transmit" side of /proc/net/dev
(stats->{tx_carrier_errors + tx_aborted_errors + tx_window_errors +
tx_heartbeat_errors} counters in rtnl_link_stats64).

### network.interface.out.compressed

compressed column on the "Transmit" side of /proc/net/dev
(stats->tx_compressed counter in rtnl_link_stats64).
Almost exclusively used for CSLIP or HDLC devices

### network.interface.total.bytes

network total (in+out) bytes from /proc/net/dev per network interface

### network.interface.total.packets

network total (in+out) packets from /proc/net/dev per network interface

### network.interface.total.errors

network total (in+out) errors from /proc/net/dev per network interface

### network.interface.total.drops

network total (in+out) drops from /proc/net/dev per network interface

### network.interface.total.mcasts

Linux does not account for outgoing mcast packets per device, so this counter
is identical to the incoming mcast metric.

### network.sockstat.total

total number of sockets used by the system.

### network.sockstat.tcp.inuse

instantaneous number of tcp sockets currently in use

### network.sockstat.tcp.orphan

instantaneous number of orphan sockets

### network.sockstat.tcp.tw

instantaneous number of sockets waiting close

### network.sockstat.tcp.alloc

instantaneous number of allocated sockets

### network.sockstat.tcp.mem

instantaneous number of used memory for tcp

### network.sockstat.udp.inuse

instantaneous number of udp sockets currently in use

### network.sockstat.udp.mem

instantaneous number of used memory for udp

### network.sockstat.udplite.inuse

instantaneous number of udplite sockets currently in use

### network.sockstat.raw.inuse

instantaneous number of raw sockets currently in use

### network.sockstat.frag.inuse

instantaneous number of frag sockets currently in use

### network.sockstat.frag.memory

nstantaneous number of used memory for frag

### network.sockstat.tcp6.inuse

instantaneous number of tcp6 sockets currently in use

### network.sockstat.udp6.inuse

instantaneous number of udp6 sockets currently in use

### network.sockstat.udplite6.inuse

instantaneous number of udplite6 sockets currently in use

### network.sockstat.raw6.inuse

instantaneous number of raw6 sockets currently in use

### network.sockstat.frag6.inuse

instantaneous number of frag6 sockets currently in use

### network.sockstat.frag6.memory

instantaneous number of used memory for frag6

### network.ip.forwarding

count of ip forwarding

### network.ip.defaultttl

count of ip defaultttl

### network.ip.inreceives

count of ip inreceives

### network.ip.inhdrerrors

count of ip inhdrerrors

### network.ip.inaddrerrors

count of ip inaddrerrors

### network.ip.forwdatagrams

count of ip forwdatagrams

### network.ip.inunknownprotos

count of ip inunknownprotos

### network.ip.indiscards

count of ip indiscards

### network.ip.indelivers

count of ip indelivers

### network.ip.outrequests

count of ip outrequests

### network.ip.outdiscards

count of ip outdiscards

### network.ip.outnoroutes

count of ip outnoroutes

### network.ip.reasmtimeout

count of ip reasmtimeout

### network.ip.reasmreqds

count of ip reasmreqds

### network.ip.reasmoks

count of ip reasmoks

### network.ip.reasmfails

count of ip reasmfails

### network.ip.fragoks

count of ip fragoks

### network.ip.fragfails

count of ip fragfails

### network.ip.fragcreates

count of ip fragcreates

### network.ip.innoroutes

Number of IP datagrams discarded due to no routes in forwarding path

### network.ip.intruncatedpkts

Number of IP datagrams discarded due to frame not carrying enough data

### network.ip.inmcastpkts

Number of received IP multicast datagrams

### network.ip.outmcastpkts

Number of sent IP multicast datagrams

### network.ip.inbcastpkts

Number of received IP broadcast datagrams

### network.ip.outbcastpkts

Number of sent IP bradcast datagrams

### network.ip.inoctets

Number of received octets

### network.ip.outoctets

Number of sent octets

### network.ip.inmcastoctets

Number of received IP multicast octets

### network.ip.outmcastoctets

Number of sent IP multicast octets

### network.ip.inbcastoctets

Number of received IP broadcast octets

### network.ip.outbcastoctets

Number of sent IP broadcast octets

### network.ip.csumerrors

Number of IP datagrams with checksum errors

### network.ip.noectpkts

Number of packets received with NOECT

### network.ip.ect1pkts

Number of packets received with ECT(1)

### network.ip.ect0pkts

Number of packets received with ECT(0)

### network.ip.cepkts

Number of packets received with Congestion Experimented

### network.icmp.inmsgs

count of icmp inmsgs

### network.icmp.inerrors

count of icmp inerrors

### network.icmp.indestunreachs

count of icmp indestunreachs

### network.icmp.intimeexcds

count of icmp intimeexcds

### network.icmp.inparmprobs

count of icmp inparmprobs

### network.icmp.insrcquenchs

count of icmp insrcquenchs

### network.icmp.inredirects

count of icmp inredirects

### network.icmp.inechos

count of icmp inechos

### network.icmp.inechoreps

count of icmp inechoreps

### network.icmp.intimestamps

count of icmp intimestamps

### network.icmp.intimestampreps

count of icmp intimestampreps

### network.icmp.inaddrmasks

count of icmp inaddrmasks

### network.icmp.inaddrmaskreps

count of icmp inaddrmaskreps

### network.icmp.outmsgs

count of icmp outmsgs

### network.icmp.outerrors

count of icmp outerrors

### network.icmp.outdestunreachs

count of icmp outdestunreachs

### network.icmp.outtimeexcds

count of icmp outtimeexcds

### network.icmp.outparmprobs

count of icmp outparmprobs

### network.icmp.outsrcquenchs

count of icmp outsrcquenchs

### network.icmp.outredirects

count of icmp outredirects

### network.icmp.outechos

count of icmp outechos

### network.icmp.outechoreps

count of icmp outechoreps

### network.icmp.outtimestamps

count of icmp outtimestamps

### network.icmp.outtimestampreps

count of icmp outtimestampreps

### network.icmp.outaddrmasks

count of icmp outaddrmasks

### network.icmp.outaddrmaskreps

count of icmp outaddrmaskreps

### network.icmp.incsumerrors

count of icmp in checksum errors

### network.icmpmsg.intype

count of icmp message types recvd

### network.icmpmsg.outtype

count of icmp message types sent

### network.tcp.rtoalgorithm

the retransmission timeout algorithm in use

### network.tcp.rtomin

minimum retransmission timeout

### network.tcp.rtomax

maximum retransmission timeout

### network.tcp.maxconn

limit on tcp connections

### network.tcp.activeopens

count of tcp activeopens

### network.tcp.passiveopens

count of tcp passiveopens

### network.tcp.attemptfails

count of tcp attemptfails

### network.tcp.estabresets

count of tcp estabresets

### network.tcp.currestab

current established tcp connections

### network.tcp.insegs

count of tcp segments received

### network.tcp.outsegs

count of tcp segments sent

### network.tcp.retranssegs

count of tcp segments retransmitted

### network.tcp.inerrs

count of tcp segments received in error

### network.tcp.outrsts

count of tcp segments sent with RST flag

### network.tcp.incsumerrors

count of tcp segments received with checksum errors

### network.tcp.syncookiessent

Number of sent SYN cookies

### network.tcp.syncookiesrecv

Number of received SYN cookies

### network.tcp.syncookiesfailed

Number of failed SYN cookies

### network.tcp.embryonicrsts

Number of resets received for embryonic SYN_RECV sockets

### network.tcp.prunecalled

Number of packets pruned from receive queue because of socket buffer overrun

### network.tcp.rcvpruned

Number of packets pruned from receive queue

### network.tcp.ofopruned

Number of packets dropped from out-of-order queue because of socket buffer overrun

### network.tcp.outofwindowicmps

Number of dropped out of window ICMPs

### network.tcp.lockdroppedicmps

Number of dropped ICMP because socket was locked

### network.tcp.arpfilter

Number of arp packets filtered

### network.tcp.timewaited

Number of TCP sockets finished time wait in fast timer

### network.tcp.timewaitrecycled

Number of time wait sockets recycled by time stamp

### network.tcp.timewaitkilled

Number of TCP sockets finished time wait in slow timer

### network.tcp.pawspassiverejected

Number of passive connections rejected because of timestamp

### network.tcp.pawsactiverejected

Number of active connections rejected because of timestamp

### network.tcp.pawsestabrejected

Number of packets rejects in established connections because of timestamp

### network.tcp.delayedacks

Number of delayed acks sent

### network.tcp.delayedacklocked

Number of delayed acks further delayed because of locked socket

### network.tcp.delayedacklost

Number of times quick ack mode was activated times

### network.tcp.listenoverflows

Number of times the listen queue of a socket overflowed

### network.tcp.listendrops

Number of SYNs to LISTEN sockets dropped

### network.tcp.prequeued

Number of packets directly queued to recvmsg prequeue

### network.tcp.directcopyfrombacklog

Number of bytes directly in process context from backlog

### network.tcp.directcopyfromprequeue

Number of bytes directly received in process context from prequeue

### network.tcp.prequeueddropped

Number of packets dropped from prequeue

### network.tcp.hphits

Number of packet headers predicted

### network.tcp.hphitstouser

Number of packets header predicted and directly queued to user

### network.tcp.pureacks

Number of acknowledgments not containing data payload received

### network.tcp.hpacks

Number of predicted acknowledgments

### network.tcp.renorecovery

Number of times recovered from packet loss due to fast retransmit

### network.tcp.sackrecovery

Number of times recovered from packet loss by selective acknowledgements

### network.tcp.sackreneging

Number of bad SACK blocks received

### network.tcp.fackreorder

Number of times detected reordering using FACK

### network.tcp.sackreorder

Number of times detected reordering using SACK

### network.tcp.renoreorder

Number of times detected reordering using reno fast retransmit

### network.tcp.tsreorder

Number of times detected reordering times using time stamp

### network.tcp.fullundo

Number of congestion windows fully recovered without slow start

### network.tcp.partialundo

Number of congestion windows partially recovered using Hoe heuristic

### network.tcp.dsackundo

Number of congestion windows recovered without slow start using DSACK

### network.tcp.lossundo

Number of congestion windows recovered without slow start after partial ack

### network.tcp.lostretransmit

Number of retransmits lost

### network.tcp.renofailures

Number of timeouts after reno fast retransmit

### network.tcp.sackfailures

Number of timeouts after SACK recovery

### network.tcp.lossfailures

Number of timeouts in loss state

### network.tcp.fastretrans

Number of fast retransmits

### network.tcp.forwardretrans

Number of forward retransmits

### network.tcp.slowstartretrans

Number of retransmits in slow start

### network.tcp.timeouts

Number of other TCP timeouts

### network.tcp.lossprobes

Number of sent TCP loss probes

### network.tcp.lossproberecovery

Number of TCP loss probe recoveries

### network.tcp.renorecoveryfail

Number of reno fast retransmits failed

### network.tcp.sackrecoveryfail

Number of SACK retransmits failed

### network.tcp.schedulerfail

Number of times receiver scheduled too late for direct processing

### network.tcp.rcvcollapsed

Number of packets collapsed in receive queue due to low socket buffer

### network.tcp.dsackoldsent

Number of DSACKs sent for old packets

### network.tcp.dsackofosent

Number of DSACKs sent for out of order packets

### network.tcp.dsackrecv

Number of DSACKs received

### network.tcp.dsackoforecv

Number of DSACKs for out of order packets received

### network.tcp.abortondata

Number of connections reset due to unexpected data

### network.tcp.abortonclose

Number of connections reset due to early user close

### network.tcp.abortonmemory

Number of connections aborted due to memory pressure

### network.tcp.abortontimeout

Number of connections aborted due to timeout

### network.tcp.abortonlinger

Number of connections aborted after user close in linger timeout

### network.tcp.abortfailed

Number of times unable to send RST due to no memory

### network.tcp.memorypressures

Numer of times TCP ran low on memory

### network.tcp.sackdiscard

Number of SACKs discarded

### network.tcp.dsackignoredold

Number of ignored old duplicate SACKs

### network.tcp.dsackignorednoundo

Number of ignored duplicate SACKs with undo_marker not set

### network.tcp.spuriousrtos

Number of FRTO's successfully detected spurious RTOs

### network.tcp.md5notfound

Number of times MD5 hash expected but not found

### network.tcp.md5unexpected

Number of times MD5 hash unexpected but found

### network.tcp.sackshifted

Number of SACKs shifted

### network.tcp.sackmerged

Number of SACKs merged

### network.tcp.sackshiftfallback

Number of SACKs fallbacks

### network.tcp.backlogdrop

Number of frames dropped because of full backlog queue

### network.tcp.minttldrop

Number of frames dropped when TTL is under the minimum

### network.tcp.deferacceptdrop

Due to SYNACK retrans count lower than defer_accept value

### network.tcp.iprpfilter

Number of packets dropped in input path because of rp_filter settings

### network.tcp.timewaitoverflow

Number of occurrences of time wait bucket overflow

### network.tcp.reqqfulldocookies

Number of times a SYNCOOKIE was replied to client

### network.tcp.reqqfulldrop

Number of times a SYN request was dropped due to disabled syncookies

### network.tcp.retransfail

Number of failed tcp_retransmit_skb() calls

### network.tcp.rcvcoalesce

Number of times tried to coalesce the receive queue

### network.tcp.ofoqueue

Number of packets queued in OFO queue

### network.tcp.ofodrop

Number of packets meant to be queued in OFO but dropped because socket rcvbuf
limit reached.

### network.tcp.ofomerge

Number of packets in OFO that were merged with other packets

### network.tcp.challengeack

Number of challenge ACKs sent (RFC 5961 3.2)

### network.tcp.synchallenge

Number of challenge ACKs sent in response to SYN packets

### network.tcp.fastopenactive

Number of successful active fast opens

### network.tcp.fastopenactivefail

Number of fast open attempts failed due to remote not accepting it or time outs

### network.tcp.fastopenpassive

Number of successful passive fast opens

### network.tcp.fastopenpassivefail

Number of passive fast open attempts failed

### network.tcp.fastopenlistenoverflow

Number of times the fastopen listen queue overflowed

### network.tcp.fastopencookiereqd

Number of fast open cookies requested

### network.tcp.spuriousrtxhostqueues

Number of times that the fast clone is not yet freed in tcp_transmit_skb()

### network.tcp.busypollrxpackets

Number of low latency application-fetched packets

### network.tcp.autocorking

Number of times stack detected skb was underused and its flush was deferred

### network.tcp.fromzerowindowadv

Number of times window went from zero to non-zero

### network.tcp.tozerowindowadv

Number of times window went from non-zero to zero

### network.tcp.wantzerowindowadv

Number of times zero window announced

### network.tcp.synretrans

Number of SYN-SYN/ACK retransmits to break down retransmissions in SYN, fast/timeout
retransmits.

### network.tcp.origdatasent

Excluding retransmission but including data-in-SYN). This counter is different from
TcpOutSegs because TcpOutSegs also tracks pure ACKs. TCPOrigDataSent is
more useful to track the TCP retransmission rate.

### network.udp.indatagrams

count of udp indatagrams

### network.udp.noports

count of udp noports

### network.udp.inerrors

count of udp inerrors

### network.udp.outdatagrams

count of udp outdatagrams

### network.udp.recvbuferrors

count of udp receive buffer errors

### network.udp.sndbuferrors

count of udp send buffer errors

### network.udp.incsumerrors

count of udp in checksum errors

### network.udplite.indatagrams

count of udplite indatagrams

### network.udplite.noports

count of udplite noports

### network.udplite.inerrors

count of udplite inerrors

### network.udplite.outdatagrams

count of udplite outdatagrams

### network.udplite.recvbuferrors

count of udplite receive buffer errors

### network.udplite.sndbuferrors

count of udplite send buffer errors

### network.udplite.incsumerrors

count of udplite in checksum errors

### network.udpconn.established

Number of established udp connections

### network.udpconn.listen

Number of udp connections in listen state

### network.rawconn.count

Number of raw socket connections

### network.tcpconn.established

Number of established connections

### network.tcpconn.syn_sent

Number of SYN_SENT connections

### network.tcpconn.syn_recv

Number of SYN_RECV connections

### network.tcpconn.fin_wait1

Number of FIN_WAIT1 connections

### network.tcpconn.fin_wait2

Number of FIN_WAIT2 connections

### network.tcpconn.time_wait

Number of TIME_WAIT connections

### network.tcpconn.close

Number of CLOSE connections

### network.tcpconn.close_wait

Number of CLOSE_WAIT connections

### network.tcpconn.last_ack

Number of LAST_ACK connections

### network.tcpconn.listen

Number of LISTEN connections

### network.tcpconn.closing

Number of CLOSING connections

### network.softnet.processed

number of packets (not including netpoll) received by the interrupt handler

### network.softnet.dropped

number of packets that were dropped because netdev_max_backlog was exceeded

### network.softnet.time_squeeze

number of times ksoftirq ran out of netdev_budget or time slice with work remaining

### network.softnet.cpu_collision

number of times that two cpus collided trying to get the device queue lock

### network.softnet.received_rps

number of times rps_trigger_softirq has been called

### network.softnet.flow_limit_count

softnet_data flow limit counter

### network.softnet.percpu.processed

number of packets (not including netpoll) received by the interrupt handler

### network.softnet.percpu.dropped

number of packets that were dropped because netdev_max_backlog was exceeded

### network.softnet.percpu.time_squeeze

number of times ksoftirq ran out of netdev_budget or time slice with work remaining

### network.softnet.percpu.cpu_collision

number of times that two cpus collided trying to get the device queue lock

### network.softnet.percpu.received_rps

number of times rps_trigger_softirq has been called

### network.softnet.percpu.flow_limit_count

The network stack has to drop packets when a receive processing a CPUs
backlog reaches netdev_max_backlog.  The flow_limit_count counter is
the number of times very active flows have dropped their traffic earlier
to maintain capacity for other less active flows.

### network.unix.datagram.count

Number of datagram unix domain sockets

### network.unix.stream.established

Number of established unix domain socket streams

### network.unix.stream.listen

Number of unix domain socket streams in listen state

### network.unix.stream.count

Number of unix domain socket streams

### network.ip6.inreceives

count of ip6 inreceives

### network.ip6.inhdrerrors

count of ip6 inhdrerrors

### network.ip6.intoobigerrors

count of ip6 intoobigerrors

### network.ip6.innoroutes

count of ip6 innoroutes

### network.ip6.inaddrerrors

count of ip6 inaddrerrors

### network.ip6.inunknownprotos

count of ip6 inunknownprotos

### network.ip6.intruncatedpkts

count of ip6 intruncatedpkts

### network.ip6.indiscards

count of ip6 indiscards

### network.ip6.indelivers

count of ip6 indelivers

### network.ip6.outforwdatagrams

count of ip6 outforwdatagrams

### network.ip6.outrequests

count of ip6 outrequests

### network.ip6.outdiscards

count of ip6 outdiscards

### network.ip6.outnoroutes

count of ip6 outnoroutes

### network.ip6.reasmtimeout

count of ip6 reasmtimeout

### network.ip6.reasmreqds

count of ip6 reassembly requireds

### network.ip6.reasmoks

count of ip6 reassembly oks

### network.ip6.reasmfails

count of ip6 reassembly failures

### network.ip6.fragoks

count of ip6 fragmentation oks

### network.ip6.fragfails

count of ip6 fragmentation failures

### network.ip6.fragcreates

count of ip6 fragmentation creations

### network.ip6.inmcastpkts

count of ip6 multicast packets in

### network.ip6.outmcastpkts

count of ip6 multicast packets out

### network.ip6.inoctets

count of ip6 octets in

### network.ip6.outoctets

count of ip6 octets out

### network.ip6.inmcastoctets

count of ip6 multicast octets in

### network.ip6.outmcastoctets

count of ip6 multicast octets out

### network.ip6.inbcastoctets

count of ip6 broadcast octets in

### network.ip6.outbcastoctets

count of ip6 broadcast octets uot

### network.ip6.innoectpkts

count of ip6 packets received with NOECT

### network.ip6.inect1pkts

count of ip6 packets received with ECT(1)

### network.ip6.inect0pkts

count of ip6 packets received with ECT(0)

### network.ip6.incepkts

count of ip6 Congestion Experimented packets in

### network.icmp6.inmsgs

count of icmp6 inmsgs

### network.icmp6.inerrors

count of icmp6 inerrors

### network.icmp6.outmsgs

count of icmp6 outmsgs

### network.icmp6.outerrors

count of icmp6 outerrors

### network.icmp6.incsumerrors

count of icmp6 incsumerrors

### network.icmp6.indestunreachs

count of icmp6 indestunreachs

### network.icmp6.inpkttoobigs

count of icmp6 inpkttoobigs

### network.icmp6.intimeexcds

count of icmp6 intimeexcds

### network.icmp6.inparmproblems

count of icmp6 inparmprobs

### network.icmp6.inechos

count of icmp6 inechos

### network.icmp6.inechoreplies

count of icmp6 inechoreplies

### network.icmp6.ingroupmembqueries

count of icmp6 ingroupmembqueries

### network.icmp6.ingroupmembresponses

count of icmp6 ingroupmembresponses

### network.icmp6.ingroupmembreductions

count of icmp6 ingroupmembreductions

### network.icmp6.inroutersolicits

count of icmp6 inroutersolicits

### network.icmp6.inrouteradvertisements

count of icmp6 inrouteradvertisements

### network.icmp6.inneighborsolicits

count of icmp6 inneighborsolicits

### network.icmp6.inneighboradvertisements

count of icmp6 inneighboradvertisements

### network.icmp6.inredirects

count of icmp6 inredirects

### network.icmp6.inmldv2reports

count of icmp6 inmldv2reports

### network.icmp6.outdestunreachs

count of icmp6 outdestunreachs

### network.icmp6.outpkttoobigs

count of icmp6 outpkttoobigs

### network.icmp6.outtimeexcds

count of icmp6 outtimeexcds

### network.icmp6.outparmproblems

count of icmp6 outparmproblems

### network.icmp6.outechos

count of icmp6 outechos

### network.icmp6.outechoreplies

count of icmp6 outechoreplies

### network.icmp6.outgroupmembqueries

count of icmp6 outgroupmembqueries

### network.icmp6.outgroupmembresponses

count of icmp6 outgroupmembresponses

### network.icmp6.outgroupmembreductions

count of icmp6 outgroupmembreductions

### network.icmp6.outroutersolicits

count of icmp6 outroutersolicits

### network.icmp6.outrouteradvertisements

count of icmp6 outrouteradvertisements

### network.icmp6.outneighborsolicits

count of icmp6 outneighborsolicits

### network.icmp6.outneighboradvertisements

count of icmp6 outneighboradvertisements

### network.icmp6.outredirects

count of icmp6 outredirects

### network.icmp6.outmldv2reports

count of icmp6 outmldv2reports

### network.udp6.indatagrams

count of udp6 indatagrams

### network.udp6.noports

count of udp6 noports

### network.udp6.inerrors

count of udp6 inerrors

### network.udp6.outdatagrams

count of udp6 outdatagrams

### network.udp6.rcvbuferrors

count of udp6 rcvbuferrors

### network.udp6.sndbuferrors

count of udp6 sndbuferrors

### network.udp6.incsumerrors

count of udp6 incsumerrors

### network.udp6.ignoredmulti

count of udp6 ignoredmulti

### network.udpconn6.established

Number of established udp6 connections

### network.udpconn6.listen

Number of udp6 connections in listen state

### network.udplite6.indatagrams

count of udplite6 indatagrams

### network.udplite6.noports

count of udplite6 noports

### network.udplite6.inerrors

count of udplite6 inerrors

### network.udplite6.outdatagrams

count of udplite6 outdatagrams

### network.udplite6.rcvbuferrors

count of udplite6 receive buffer errors

### network.udplite6.sndbuferrors

count of udplite6 send buffer errors

### network.udplite6.incsumerrors

count of udplite6 in checksum errors

### network.rawconn6.count

Number of raw6 socket connections

### network.tcpconn6.established

Number of established tcp6 connections

### network.tcpconn6.syn_sent

Number of SYN_SENT tcp6 connections

### network.tcpconn6.syn_recv

Number of SYN_RECV tcp6 connections

### network.tcpconn6.fin_wait1

Number of FIN_WAIT1 tcp6 connections

### network.tcpconn6.fin_wait2

Number of FIN_WAIT2 tcp6 connections

### network.tcpconn6.time_wait

Number of TIME_WAIT tcp6 connections

### network.tcpconn6.close

Number of CLOSE tcp6 connections

### network.tcpconn6.close_wait

Number of CLOSE_WAIT tcp6 connections

### network.tcpconn6.last_ack

Number of LAST_ACK tcp6 connections

### network.tcpconn6.listen

Number of LISTEN tcp6 connections

### network.tcpconn6.closing

Number of CLOSING tcp6 connections

### network.mptcp.mpcapablesynrx

Multipath TCP received SYN with MP_CAPABLE

### network.mptcp.mpcapableackrx

Multipath TCP received third ACK with MP_CAPABLE

### network.mptcp.mpcapablefallbackack

Multipath TCP server-side fallback during 3-way handshake

### network.mptcp.mpcapablefallbacksynack

Multipath TCP client-side fallback during 3-way handshake

### network.mptcp.mptcpretrans

Multipath TCP segments retransmitted at the MPTCP-level

### network.mptcp.mpjoinnotokenfound

Multipath TCP received MP_JOIN but the token was not found

### network.mptcp.mpjoinsynrx

Multipath TCP received a SYN and MP_JOIN

### network.mptcp.mpjoinsynackrx

Multipath TCP received a SYN/ACK and MP_JOIN

### network.mptcp.mpjoinsynackhmacfailure

Multipath TCP HMAC was wrong on SYN/ACK and MP_JOIN

### network.mptcp.mpjoinackrx

Multipath TCP received an ACK and MP_JOIN

### network.mptcp.mpjoinackhmacfailure

Multipath TCP HMAC was wrong on ACK and MP_JOIN

### network.mptcp.dssnotmatching

Multipath TCP received a new mapping that did not match the previous one

### network.mptcp.infinitemaprx

Multipath TCP received an infinite mapping
## ipc

### ipc.sem.max_semmap

maximum number of entries in a semaphore map (from semctl(..,IPC_INFO,..))

### ipc.sem.max_semid

maximum number of semaphore identifiers (from semctl(..,IPC_INFO,..))

### ipc.sem.max_sem

maximum number of semaphores in system (from semctl(..,IPC_INFO,..))

### ipc.sem.num_undo

number of undo structures in system (from semctl(..,IPC_INFO,..))

### ipc.sem.max_perid

maximum number of semaphores per identifier (from semctl(..,IPC_INFO,..))

### ipc.sem.max_ops

maximum number of operations per semop call (from semctl(..,IPC_INFO,..))

### ipc.sem.max_undoent

maximum number of undo entries per process (from semctl(..,IPC_INFO,..))

### ipc.sem.sz_semundo

size of struct sem_undo (from semctl(..,IPC_INFO,..))

### ipc.sem.max_semval

semaphore maximum value (from semctl(..,IPC_INFO,..))

### ipc.sem.max_exit

adjust on exit maximum value (from semctl(..,IPC_INFO,..))

### ipc.sem.used_sem

number of semaphore sets currently on the system (from semctl(..,SEM_INFO,..))

### ipc.sem.tot_sem

number of semaphores in all sets on the system (from semctl(..,SEM_INFO,..))

### ipc.sem.key

key of these semaphore (from msgctl(..,SEM_STAT,..))

### ipc.sem.owner

username of owner (from msgctl(..,SEM_STAT,..))

### ipc.sem.perms

access permissions (from msgctl(..,SEM_STAT,..))

### ipc.sem.nsems

number of semaphore (from semctl(..,SEM_STAT,..))

### ipc.msg.sz_pool

size of message pool in kilobytes (from msgctl(..,IPC_INFO,..))

### ipc.msg.mapent

number of entries in a message map (from msgctl(..,IPC_INFO,..))

### ipc.msg.max_msgsz

maximum size of a message in bytes (from msgctl(..,IPC_INFO,..))

### ipc.msg.max_defmsgq

default maximum size of a message queue (from msgctl(..,IPC_INFO,..))

### ipc.msg.max_msgqid

maximum number of message queue identifiers (from msgctl(..,IPC_INFO,..))

### ipc.msg.max_msgseg

message segment size (from msgctl(..,IPC_INFO,..))

### ipc.msg.num_smsghdr

number of system message headers (from msgctl(..,IPC_INFO,..))

### ipc.msg.max_seg

maximum number of message segments (from msgctl(..,IPC_INFO,..))

### ipc.msg.used_queues

number of message queues that currently exist (from msgctl(..,MSG_INFO,..))

### ipc.msg.tot_msg

total number of messages in all queues (from msgctl(..,MSG_INFO,..))

### ipc.msg.tot_bytes

number of bytes in all messages in all queues (from msgctl(..,MSG_INFO,..))

### ipc.msg.key

name of these messages slot (from msgctl(..,MSG_STAT,..))

### ipc.msg.owner

username of owner (from msgctl(..,MSG_STAT,..))

### ipc.msg.perms

access permissions (from msgctl(..,MSG_STAT,..))

### ipc.msg.msgsz

used size in bytes (from msgctl(..,MSG_STAT,..))

### ipc.msg.messages

number of messages currently queued (from msgctl(..,MSG_STAT,..))

### ipc.msg.last_send_pid

last process to send on each message queue

### ipc.msg.last_recv_pid

last process to recv on each message queue

### ipc.shm.max_segsz

maximum shared segment size in bytes (from shmctl(..,IPC_INFO,..))

### ipc.shm.min_segsz

minimum shared segment size in bytes (from shmctl(..,IPC_INFO,..))

### ipc.shm.max_seg

maximum number of shared segments in system (from shmctl(..,IPC_INFO,..))

### ipc.shm.max_segproc

maximum number of shared segments per process (from shmctl(..,IPC_INFO,..))

### ipc.shm.max_shmsys

maximum amount of shared memory in system in pages (from shmctl(..,IPC_INFO,..))

### ipc.shm.tot

total number of shared memory pages (from shmctl(..,SHM_INFO,..))

### ipc.shm.rss

number of resident shared memory pages (from shmctl(..,SHM_INFO,..))

### ipc.shm.swp

number of swapped shared memory pages (from shmctl(..,SHM_INFO,..))

### ipc.shm.used_ids

number of currently existing segments (from shmctl(..,SHM_INFO,..))

### ipc.shm.swap_attempts

number of swap attempts (from shmctl(..,SHM_INFO,..))

### ipc.shm.swap_successes

number of swap successes (from shmctl(..,SHM_INFO,..))

### ipc.shm.key

Key supplied to shmget (from shmctl(.., SHM_STAT, ..))

### ipc.shm.owner

share memory segment owner (rom shmctl(.., SHM_STAT, ..))

### ipc.shm.perms

operation perms (from shmctl(.., SHM_STAT, ..))

### ipc.shm.segsz

size of segment (bytes) (from shmctl(.., SHM_STAT, ..))

### ipc.shm.nattch

no. of current attaches (from shmctl(.., SHM_STAT, ..))

### ipc.shm.status

The string value may contain the space-separated values "dest" (a shared memory
segment marked for destruction on last detach) and "locked" or the empty string.

### ipc.shm.creator_pid

process creating each shared memory segment

### ipc.shm.last_access_pid

process last accessing each shared memory segment
## vfs

### vfs.files.count

number of in-use file structures

### vfs.files.free

number of available file structures

### vfs.files.max

hard maximum on number of file structures

### vfs.inodes.count

number of in-use inode structures

### vfs.inodes.free

number of available inode structures

### vfs.dentry.count

number of in-use directory entry structures

### vfs.dentry.free

number of available directory entry structures

### vfs.aio.count

number of in-use asynchronous IO structures

### vfs.aio.max

hard maximum on number of asynchronous IO structures

### vfs.locks.posix.read

number of POSIX locks held for reading

### vfs.locks.posix.write

number of POSIX locks held for writing

### vfs.locks.posix.count

number of POSIX lock structures

### vfs.locks.flock.read

number of advisory file locks held for reading

### vfs.locks.flock.write

number of advisory file locks held for writing

### vfs.locks.flock.count

number of advisory file lock structures

### vfs.locks.lease.read

number of file leases held for reading

### vfs.locks.lease.write

number of file leases held for writing

### vfs.locks.lease.count

number of file lease structures
## sysfs

### sysfs.kernel.uevent_seqnum

counter of the number of uevents processed by the udev subsystem
## tmpfs

### tmpfs.capacity

Total capacity of mounted tmpfs filesystem (Kbytes)

### tmpfs.used

Total space used on mounted tmpfs filesystem (Kbytes)

### tmpfs.free

Total space free on mounted tmpfs filesystem (Kbytes)

### tmpfs.maxfiles

Inodes capacity of mounted tmpfs filesystem

### tmpfs.usedfiles

Number of inodes allocated on mounted tmpfs filesystem

### tmpfs.freefiles

Number of unallocated inodes on mounted tmpfs filesystem

### tmpfs.full

Percentage of tmpfs filesystem in use
## containers

### containers.engine

technology backing each container (e.g. docker)

### containers.name

mapping of unique container IDs to human-readable names

### containers.pid

process identifier for each containers initial process

### containers.cgroup

path mapping container names to their cgroups

### containers.state.running

this container is currently running (one/zero)

### containers.state.paused

this container is currently paused (one/zero)

### containers.state.restarting

this container is restarting (one/zero)
## nvidia

### nvidia.numcards

The number of NVIDIA Graphics cards installed in this system

### nvidia.gpuid

Zero indexed id of this NVIDIA card

### nvidia.cardname

The name of the graphics card

### nvidia.busid

The Bus ID as reported by the NVIDIA tools, not lspci

### nvidia.temp

The Temperature of the GPU on the NVIDIA card in degrees celcius.

### nvidia.fanspeed

Speed of the GPU fan as a percentage of the maximum

### nvidia.perfstate

The PX performance state as reported from NVML.  Value is an integer
which should range from 0 (maximum performance) to 15 (minimum).  If
the state is unknown the reported value will be 32, however.

### nvidia.gpuactive

Percentage of time over the past sample period during which one or more
kernels was executing on the GPU.

### nvidia.memactive

Percent of time over the past sample period during which global (device)
memory was being read or written.  This metric shows if the memory is
actively being accesed, and is not correlated to storage amount used.

### nvidia.memused

Amount of GPU FB memory that has currently been allocated, in bytes.
Note that the driver/GPU always sets aside a small amount of memory
for bookkeeping. 

### nvidia.memtotal

The total amount of GPU FB memory available on the card, in bytes.

### nvidia.memfree

Amount of GPU FB memory that is not currently allocated, in bytes.

### nvidia.proc.samples

Number of times process stats have been sampled

### nvidia.proc.memused

Memory in use by each process accessing each card

### nvidia.proc.memaccum

Accumulated memory used by processes accessing each card

### nvidia.proc.gpuactive

Graphics card utilization by processes accessing each card

### nvidia.proc.memactive

Memory access utilization by processes accessing each card

### nvidia.proc.time

Milliseconds spent by processes accessing each graphics card
## nfs4

### nfs4.client.calls

cumulative total of client NFSv4 requests

### nfs4.client.reqs

cumulative total for each client NFSv4 request type

### nfs4.server.calls

cumulative total of server NFSv4 operations, plus NULL requests

### nfs4.server.reqs

cumulative total for each server NFSv4 operation, and for NULL requests
## cgroup

### cgroup.subsys.hierarchy

subsystem hierarchy from /proc/cgroups

### cgroup.subsys.count

count of known subsystems in /proc/cgroups

### cgroup.subsys.num_cgroups

number of cgroups for each subsystem

### cgroup.subsys.enabled

state of cgroups subsystems in the kernel

### cgroup.mounts.subsys

mount points for each cgroup subsystem

### cgroup.mounts.count

count of cgroup filesystem mount points

### cgroup.cpu.stat.user

Time spent by tasks of the cgroup in user mode

### cgroup.cpu.stat.system

Time spent by tasks of the cgroup in kernel mode

### cgroup.cpu.stat.usage

CPU time consumed by processes in each cgroup

### cgroup.cpuset.cpus

CPUs assigned to each individual cgroup

### cgroup.cpuset.mems

Memory nodes assigned to each individual cgroup

### cgroup.cpuset.id.container

Each cpuset cgroups container based on heuristics

### cgroup.cpuacct.usage

CPU time consumed by processes in each cgroup

### cgroup.cpuacct.usage_percpu

Per-CPU time consumed by processes in each cgroup

### cgroup.cpuacct.stat.user

Time spent by tasks of the cgroup in user mode

### cgroup.cpuacct.stat.system

Time spent by tasks of the cgroup in kernel mode

### cgroup.cpuacct.id.container

Each cpuacct cgroups container based on heuristics

### cgroup.cpusched.shares

Scheduler fairness CPU time division for each cgroup - details in
Documentation/scheduler/sched-design-CFS.txt in the kernel source.

### cgroup.cpusched.periods

Scheduler group bandwidth enforcement interfaces that have elapsed,
refer to Documentation/scheduler/sched-bwc.txt in the kernel source.

### cgroup.cpusched.throttled

Scheduler group bandwidth throttle/limit count - further discussion
in Documentation/scheduler/sched-bwc.txt in the kernel source.

### cgroup.cpusched.throttled_time

The total time duration (in nanoseconds) for which entities of the
group have been throttled by the CFS scheduler - refer to discussion
in Documentation/scheduler/sched-bwc.txt in the kernel source.

### cgroup.cpusched.cfs_period

The bandwidth allowed for a CFS group is specified using a quota and period.
Within each given "period" (usec), a group is allowed to consume only up to
"quota" usec of CPU time.  When the CPU bandwidth consumption of a group
exceeds this limit (for that period), the tasks belonging to its hierarchy
will be throttled and are not allowed to run again until the next period.
Further discussion in Documentation/scheduler/sched-bwc.txt in the kernel
sources.

### cgroup.cpusched.cfs_quota

The bandwidth allowed for a CFS group is specified using a quota and period.
Within each given "period" (usec), a group is allowed to consume only up to
"quota" usec of CPU time.  When the CPU bandwidth consumption of a group
exceeds this limit (for that period), the tasks belonging to its hierarchy
will be throttled and are not allowed to run again until the next period.

A value of -1 indicates that the group does not have bandwidth restriction
in place.  Refer to discussion in Documentation/scheduler/sched-bwc.txt in
the kernel source.

### cgroup.cpusched.id.container

Each cpusched cgroups container based on heuristics

### cgroup.memory.usage

Current physical memory accounted to each cgroup

### cgroup.memory.limit

Maximum memory that can be utilized by each cgroup

### cgroup.memory.failcnt

Count of failures to allocate memory due to cgroup limit

### cgroup.memory.current

The total amount of memory currently being used by the cgroup and its descendants

### cgroup.memory.stat.cache

Number of bytes of page cache memory

### cgroup.memory.stat.rss

Anonymous and swap memory (incl transparent hugepages)

### cgroup.memory.stat.rss_huge

Anonymous transparent hugepages

### cgroup.memory.stat.mapped_file

Bytes of mapped file (incl tmpfs/shmem)

### cgroup.memory.stat.writeback

Bytes of file/anonymous cache queued for syncing

### cgroup.memory.stat.swap

Number of bytes of swap usage

### cgroup.memory.stat.pgpgin

Number of charging events to the memory cgroup. The charging event happens
each time a page is accounted as either mapped anon page(RSS) or cache page
(Page Cache) to the cgroup.

### cgroup.memory.stat.pgpgout

The uncharging event happens each time a page is unaccounted from
the cgroup.

### cgroup.memory.stat.pgfault

Total number of page faults

### cgroup.memory.stat.pgmajfault

Number of major page faults

### cgroup.memory.stat.inactive_anon

Anonymous and swap cache memory on inactive LRU list

### cgroup.memory.stat.active_anon

Anonymous and swap cache memory on active LRU list.

### cgroup.memory.stat.inactive_file

File-backed memory on inactive LRU list

### cgroup.memory.stat.active_file

File-backed memory on active LRU list

### cgroup.memory.stat.unevictable

Memory that cannot be reclaimed (e.g. mlocked)

### cgroup.memory.stat.anon

Anonymous memory

### cgroup.memory.stat.anon_thp

Anonymous memory in transparent huge pages for each cgroup

### cgroup.memory.stat.file

Bytes of cached file data total for each cgroup

### cgroup.memory.stat.file_dirty

Bytes of dirty cached file data for each cgroup

### cgroup.memory.stat.file_mapped

Bytes of mapped file data for each cgroup

### cgroup.memory.stat.file_writeback

Bytes of file data under writeback for each cgroup

### cgroup.memory.stat.kernel_stack

Bytes of kernel stack memory for each cgroup

### cgroup.memory.stat.pgactivate

Activated pages for each cgroup

### cgroup.memory.stat.pgdeactivate

Deactivated pages for each cgroup

### cgroup.memory.stat.pglazyfree

Pages being lazily freed for each cgroup

### cgroup.memory.stat.pglazyfreed

Pages lazily freed for each cgroup

### cgroup.memory.stat.pgrefill

Refill pages for each cgroup

### cgroup.memory.stat.pgscan

Scanned pages for each cgroup

### cgroup.memory.stat.pgsteal

Steal pages for each cgroup

### cgroup.memory.stat.shmem

Shared memory for each cgroup

### cgroup.memory.stat.slab

Total slab pages for each cgroup

### cgroup.memory.stat.slab_reclaimable

Reclaimable slab pages for each cgroup

### cgroup.memory.stat.slab_unreclaimable

Unreclaimable slab pages for each cgroup

### cgroup.memory.stat.sock

Pages in each cgroup used for sockets

### cgroup.memory.stat.thp_collapse_alloc

Transparent huge page collapses for each cgroup

### cgroup.memory.stat.thp_fault_alloc

Transparent huge page faults for each cgroup

### cgroup.memory.stat.total.cache

Hierarchical, cumulative version of stat.cache

### cgroup.memory.stat.total.rss

Hierarchical, cumulative version of stat.rss

### cgroup.memory.stat.total.rss_huge

Hierarchical, cumulative version of stat.rss_huge

### cgroup.memory.stat.total.mapped_file

Hierarchical, cumulative version of stat.mapped_file

### cgroup.memory.stat.total.writeback

Hierarchical, cumulative version of stat.writeback

### cgroup.memory.stat.total.swap

Hierarchical, cumulative version of stat.swap

### cgroup.memory.stat.total.pgpgin

Hierarchical, cumulative version of stat.pgpgin

### cgroup.memory.stat.total.pgpgout

Hierarchical, cumulative version of stat.pgpgout

### cgroup.memory.stat.total.pgfault

Hierarchical, cumulative version of stat.pgfault

### cgroup.memory.stat.total.pgmajfault

Hierarchical, cumulative version of stat.pgmajfault

### cgroup.memory.stat.total.inactive_anon

Hierarchical, cumulative version of stat.inactive_anon

### cgroup.memory.stat.total.active_anon

Hierarchical, cumulative version of stat.active_anon

### cgroup.memory.stat.total.inactive_file

Hierarchical, cumulative version of stat.inactive_file

### cgroup.memory.stat.total.active_file

Hierarchical, cumulative version of stat.active_file

### cgroup.memory.stat.total.unevictable

Hierarchical, cumulative version of stat.unevictable

### cgroup.memory.stat.recent.rotated_anon

VM internal parameter (see mm/vmscan.c)

### cgroup.memory.stat.recent.rotated_file

VM internal parameter (see mm/vmscan.c)

### cgroup.memory.stat.recent.scanned_anon

VM internal parameter (see mm/vmscan.c)

### cgroup.memory.stat.recent.scanned_file

VM internal parameter (see mm/vmscan.c)

### cgroup.memory.stat.workingset.activate

Activated working set pages for each cgroup

### cgroup.memory.stat.workingset.nodereclaim

Working set pages under NUMA node reclaim for each cgroup

### cgroup.memory.stat.workingset.refault

Refault working set pages for each cgroup

### cgroup.memory.id.container

Each memory cgroups container based on heuristics

### cgroup.netclass.classid

Network classifier cgroup class identifiers

### cgroup.netclass.id.container

Each netclass cgroups container based on heuristics

### cgroup.blkio.dev.sectors

Per-cgroup total (read+write) sectors

### cgroup.blkio.dev.time

Per-device, per-cgroup total (read+write) time

### cgroup.blkio.dev.io_merged.read

Per-cgroup read merges

### cgroup.blkio.dev.io_merged.write

Per-cgroup write merges

### cgroup.blkio.dev.io_merged.sync

Per-cgroup synchronous merges 

### cgroup.blkio.dev.io_merged.async

Per-cgroup asynchronous merges

### cgroup.blkio.dev.io_merged.total

Per-cgroup total merge operations

### cgroup.blkio.dev.io_queued.read

Per-cgroup queued read operations

### cgroup.blkio.dev.io_queued.write

Per-cgroup queued write operations

### cgroup.blkio.dev.io_queued.sync

Per-cgroup queued synchronous operations

### cgroup.blkio.dev.io_queued.async

Per-cgroup queued asynchronous operations

### cgroup.blkio.dev.io_queued.total

Per-cgroup total operations queued

### cgroup.blkio.dev.io_service_bytes.read

Per-cgroup bytes transferred in reads

### cgroup.blkio.dev.io_service_bytes.write

Per-cgroup bytes transferred to disk in writes

### cgroup.blkio.dev.io_service_bytes.sync

Per-cgroup sync bytes transferred

### cgroup.blkio.dev.io_service_bytes.async

Per-cgroup async bytes transferred

### cgroup.blkio.dev.io_service_bytes.total

Per-cgroup total bytes transferred

### cgroup.blkio.dev.io_serviced.read

Per-cgroup read operations serviced

### cgroup.blkio.dev.io_serviced.write

Per-cgroup write operations serviced

### cgroup.blkio.dev.io_serviced.sync

Per-cgroup sync operations serviced

### cgroup.blkio.dev.io_serviced.async

Per-cgroup async operations serviced

### cgroup.blkio.dev.io_serviced.total

Per-cgroup total operations serviced

### cgroup.blkio.dev.io_service_time.read

Per-cgroup read IO service time

### cgroup.blkio.dev.io_service_time.write

Per-cgroup write IO service time

### cgroup.blkio.dev.io_service_time.sync

Per-cgroup sync IO service time

### cgroup.blkio.dev.io_service_time.async

Per-cgroup async IO service time

### cgroup.blkio.dev.io_service_time.total

Per-cgroup IO service time

### cgroup.blkio.dev.io_wait_time.read

Per-cgroup read IO wait time

### cgroup.blkio.dev.io_wait_time.write

Per-cgroup write IO wait time

### cgroup.blkio.dev.io_wait_time.sync

Per-cgroup sync IO wait time

### cgroup.blkio.dev.io_wait_time.async

Per-cgroup async IO wait time

### cgroup.blkio.dev.io_wait_time.total

Per-cgroup total IO wait time

### cgroup.blkio.dev.throttle.io_service_bytes.read

Per-cgroup throttle bytes transferred in reads

### cgroup.blkio.dev.throttle.io_service_bytes.write

Per-cgroup throttle bytes transferred to disk in writes

### cgroup.blkio.dev.throttle.io_service_bytes.sync

Per-cgroup throttle sync bytes transferred

### cgroup.blkio.dev.throttle.io_service_bytes.async

Per-cgroup throttle async bytes transferred

### cgroup.blkio.dev.throttle.io_service_bytes.total

Per-cgroup total throttle bytes transferred

### cgroup.blkio.dev.throttle.io_serviced.read

Per-cgroup throttle read operations serviced

### cgroup.blkio.dev.throttle.io_serviced.write

Per-cgroup throttle write operations serviced

### cgroup.blkio.dev.throttle.io_serviced.sync

Per-cgroup throttle sync operations serviced

### cgroup.blkio.dev.throttle.io_serviced.async

Per-cgroup throttle async operations serviced

### cgroup.blkio.dev.throttle.io_serviced.total

Per-cgroup total throttle operations serviced

### cgroup.blkio.all.sectors

Per-cgroup total (read+write) sectors

### cgroup.blkio.all.time

Per-device, per-cgroup total (read+write) time

### cgroup.blkio.all.io_merged.read

Per-cgroup read merges

### cgroup.blkio.all.io_merged.write

Per-cgroup write merges

### cgroup.blkio.all.io_merged.sync

Per-cgroup synchronous merges 

### cgroup.blkio.all.io_merged.async

Per-cgroup asynchronous merges

### cgroup.blkio.all.io_merged.total

Per-cgroup total merge operations

### cgroup.blkio.all.io_queued.read

Per-cgroup queued read operations

### cgroup.blkio.all.io_queued.write

Per-cgroup queued write operations

### cgroup.blkio.all.io_queued.sync

Per-cgroup queued synchronous operations

### cgroup.blkio.all.io_queued.async

Per-cgroup queued asynchronous operations

### cgroup.blkio.all.io_queued.total

Per-cgroup total operations queued

### cgroup.blkio.all.io_service_bytes.read

Per-cgroup bytes transferred in reads

### cgroup.blkio.all.io_service_bytes.write

Per-cgroup bytes transferred to disk in writes

### cgroup.blkio.all.io_service_bytes.sync

Per-cgroup sync bytes transferred

### cgroup.blkio.all.io_service_bytes.async

Per-cgroup async bytes transferred

### cgroup.blkio.all.io_service_bytes.total

Per-cgroup total bytes transferred

### cgroup.blkio.all.io_serviced.read

Per-cgroup read operations serviced

### cgroup.blkio.all.io_serviced.write

Per-cgroup write operations serviced

### cgroup.blkio.all.io_serviced.sync

Per-cgroup sync operations serviced

### cgroup.blkio.all.io_serviced.async

Per-cgroup async operations serviced

### cgroup.blkio.all.io_serviced.total

Per-cgroup total operations serviced

### cgroup.blkio.all.io_service_time.read

Per-cgroup read IO service time

### cgroup.blkio.all.io_service_time.write

Per-cgroup write IO service time

### cgroup.blkio.all.io_service_time.sync

Per-cgroup sync IO service time

### cgroup.blkio.all.io_service_time.async

Per-cgroup async IO service time

### cgroup.blkio.all.io_service_time.total

Per-cgroup IO service time

### cgroup.blkio.all.io_wait_time.read

Per-cgroup read IO wait time

### cgroup.blkio.all.io_wait_time.write

Per-cgroup write IO wait time

### cgroup.blkio.all.io_wait_time.sync

Per-cgroup sync IO wait time

### cgroup.blkio.all.io_wait_time.async

Per-cgroup async IO wait time

### cgroup.blkio.all.io_wait_time.total

Per-cgroup total IO wait time

### cgroup.blkio.all.throttle.io_service_bytes.read

Per-cgroup throttle bytes transferred in reads

### cgroup.blkio.all.throttle.io_service_bytes.write

Per-cgroup throttle bytes transferred to disk in writes

### cgroup.blkio.all.throttle.io_service_bytes.sync

Per-cgroup throttle sync bytes transferred

### cgroup.blkio.all.throttle.io_service_bytes.async

Per-cgroup throttle async bytes transferred

### cgroup.blkio.all.throttle.io_service_bytes.total

Per-cgroup throttle total bytes transferred

### cgroup.blkio.all.throttle.io_serviced.read

Per-cgroup throttle read operations serviced

### cgroup.blkio.all.throttle.io_serviced.write

Per-cgroup throttle write operations serviced

### cgroup.blkio.all.throttle.io_serviced.sync

Per-cgroup throttle sync operations serviced

### cgroup.blkio.all.throttle.io_serviced.async

Per-cgroup throttle async operations serviced

### cgroup.blkio.all.throttle.io_serviced.total

Per-cgroup total throttle operations serviced

### cgroup.blkio.id.container

Each blkio cgroups container based on heuristics

### cgroup.pressure.cpu.some.avg10sec

Indicates the time in which at least some cgroup tasks stalled on CPU
resources over the last 10 seconds.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name cpu.pressure

### cgroup.pressure.cpu.some.avg1min

Indicates the time in which at least some cgroup tasks stalled on CPU
resources over the last 1 minute.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name cpu.pressure

### cgroup.pressure.cpu.some.avg5min

Indicates the time in which at least some cgroup tasks stalled on CPU
resources over the last 5 minutes.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name cpu.pressure

### cgroup.pressure.cpu.some.total

Indicates the time in which at least some cgroup tasks stalled on CPU
resources (total time, cumulative).  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name cpu.pressure

### cgroup.pressure.memory.some.avg10sec

Indicates the time in which at least some cgroup tasks stalled on memory
resources over the last 10 seconds.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name memory.pressure

### cgroup.pressure.memory.some.avg1min

Indicates the time in which at least some cgroup tasks stalled on memory
resources over the last 1 minute.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name memory.pressure

### cgroup.pressure.memory.some.avg5min

Indicates the time in which at least some cgroup tasks stalled on memory
resources over the last 5 minutes.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name memory.pressure

### cgroup.pressure.memory.some.total

The CPU time for which at least some cgroup tasks stalled on memory
resources.  Pressure stall information (PSI) from:
$ find /sys/fs/cgroup -name memory.pressure

### cgroup.pressure.memory.full.avg10sec

Indicates the time in which all cgroup tasks stalled on memory
resources over the last 10 seconds.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name memory.pressure

### cgroup.pressure.memory.full.avg1min

Indicates the time in which all cgroup tasks stalled on memory
resources over the last 1 minute.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name memory.pressure

### cgroup.pressure.memory.full.avg5min

Indicates the time in which all cgroup tasks stalled on memory
resources over the last 5 minutes.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name memory.pressure

### cgroup.pressure.memory.full.total

The CPU time for which all cgroup tasks stalled on memory resources.
Pressure stall information (PSI) from:
$ find /sys/fs/cgroup -name memory.pressure

### cgroup.pressure.io.some.avg10sec

Indicates the time in which at least some cgroup tasks stalled on IO
resources over the last 10 seconds.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name io.pressure

### cgroup.pressure.io.some.avg1min

Indicates the time in which at least some cgroup tasks stalled on IO
resources over the last 1 minute.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name io.pressure

### cgroup.pressure.io.some.avg5min

Indicates the time in which at least some cgroup tasks stalled on IO
resources over the last 5 minutes.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name io.pressure

### cgroup.pressure.io.some.total

The CPU time in which at least some cgroup tasks stalled on IO
resources.  Pressure stall information (PSI) from:
$ find /sys/fs/cgroup -name io.pressure

### cgroup.pressure.io.full.avg10sec

Indicates the time in which all cgroup tasks stalled on input/output
resources over the last 10 seconds.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name io.pressure

### cgroup.pressure.io.full.avg1min

Indicates the time in which all cgroup tasks stalled on input/output
resources over the last 1 minute.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name io.pressure

### cgroup.pressure.io.full.avg5min

Indicates the time in which all cgroup tasks stalled on input/output
resources over the last 5 minutes.  Pressure stall information (PSI)
from: $ find /sys/fs/cgroup -name io.pressure

### cgroup.pressure.io.full.total

The CPU time in which all cgroup tasks stalled on IO resources.
Pressure stall information (PSI) from:
$ find /sys/fs/cgroup -name io.pressure

### cgroup.io.stat.rbytes

Bytes read per-cgroup, per-device

### cgroup.io.stat.wbytes

Bytes written per-cgroup, per-device

### cgroup.io.stat.rios

Read operations per-cgroup, per-device

### cgroup.io.stat.wios

Write operations per-cgroup, per-device

### cgroup.io.stat.dbytes

Direct IO bytes per-cgroup, per-device

### cgroup.io.stat.dios

Direct IO operations per-cgroup, per-device
## acct

### acct.psinfo.tty

Controlling terminal device number

### acct.psinfo.exitcode

Process termination status

### acct.psinfo.pid

Process ID

### acct.psinfo.ppid

Parent process ID

### acct.psinfo.btime

Process creation time

### acct.psinfo.etime

Elapsed time

### acct.psinfo.utime

User CPU time

### acct.psinfo.stime

System CPU time

### acct.psinfo.mem

Average memory usage

### acct.psinfo.io

Characters transferred

### acct.psinfo.rw

Blocks read or written

### acct.psinfo.minflt

Minor page faults

### acct.psinfo.majflt

Major page faults

### acct.psinfo.swaps

Number of swaps

### acct.psinfo.ttyname

Controlling terminal name

### acct.id.uid

Real user ID

### acct.id.gid

Real group ID

### acct.id.uid_nm

Real user name

### acct.id.gid_nm

Real group name

### acct.flag.fork

Executed fork but no exec (boolean)

### acct.flag.su

Used superuser privileges (boolean)

### acct.flag.core

Dumped core (boolean)

### acct.flag.xsig

Killed by a signal (boolean)

### acct.control.open_retry_interval

Minimal time to retry open after failing to open acct file

### acct.control.check_acct_interval

Interval to check if process accounting works

### acct.control.file_size_threshold

Size at which the acct file will be reopened

### acct.control.lifetime

Period of holding acct information after process exits

### acct.control.refresh

Interval to check if private acct file should be reopened

### acct.control.enable_acct

Boolean for whether to open private acct file and to use acct(2) syscall
## kvm

### kvm.trace.kvm_vcpu_wakeup

KVM trace point values from /sys/kernel/debug/tracing/events/kvm files

### kvm.trace.kvm_hypercall

KVM trace point values from /sys/kernel/debug/tracing/events/kvm files

### kvm.trace.kvm_mmio

KVM trace point values from /sys/kernel/debug/tracing/events/kvm files

### kvm.trace.kvm_entry

KVM trace point values from /sys/kernel/debug/tracing/events/kvm files

### kvm.trace.kvm_exit

KVM trace point values from /sys/kernel/debug/tracing/events/kvm files

### kvm.trace.count

Number of KVM trace points from /var/lib/pcp/pmdas/kvm/kvm.conf

### kvm.efer_reload

Number of Extended Feature Enable Register (EFER) reloads.

### kvm.exits

Number of guest exits from I/O port accesses. 

### kvm.fpu_reload

Number of reload fpu(Float Point Unit).

### kvm.halt_attempted_poll

Number of times the vcpu attempts to polls.

### kvm.halt_exits

This type of exit is usually seen when a guest is idle.

### kvm.halt_successful_poll

The number of times the vcpu attempts to polls successfully.

### kvm.halt_wakeup

Number of wakeups from a halt.

### kvm.host_state_reload

Currently tallies MSR setup and guest MSR reads.

### kvm.hypercalls

Number of guest hypervisor service calls.

### kvm.insn_emulation

Number of insn_emulation attempts.

### kvm.insn_emulation_fail

Number of failed insn_emulation attempts.

### kvm.invlpg

Number of invlpg attepts. 

### kvm.io_exits

Number of guest exits from I/O port accesses.

### kvm.irq_exits

Number of guest exits due to external interrupts.

### kvm.irq_injections

Number of interrupts sent to guests.

### kvm.irq_window

Number of guest exits from an outstanding interrupt window.

### kvm.largepages

Number of large pages currently in use.

### kvm.mmio_exits

Number of guest exits due to memory mapped I/O (MMIO) accesses.

### kvm.mmu_cache_miss

Number of cache miss.

### kvm.mmu_flooded

This counts detected write operations not of individual write operations.

### kvm.mmu_pde_zapped

Number of page directory entry (PDE) destruction operations.

### kvm.mmu_pte_updated

Number of PTE updated. 

### kvm.mmu_pte_write

Number of PTE write.

### kvm.mmu_recycled

Number of shadow pages that can be reclaimed.

### kvm.mmu_shadow_zapped

Number of shadow pages that has been zapped.

### kvm.mmu_unsync

Number of non-synchronized pages which are not yet unlinked 

### kvm.nmi_injections

Number of Non-maskable Interrupt (NMI) injections.

### kvm.nmi_window

Number of guest exits from (outstanding) Non-maskable Interrupt (NMI) windows.

### kvm.pf_fixed

Number of fixed (non-paging) page table entry (PTE) maps.

### kvm.pf_guest

Number of page faults injected into guests.

### kvm.remote_tlb_flush

Number of tlb_flush operations performed by the hypervisor.

### kvm.request_irq

Number of guest interrupt window request exits.

### kvm.signal_exits

Number of guest exits due to pending signals from the host.

### kvm.tlb_flush

Number of tlb_flush operations performed by the hypervisor.
