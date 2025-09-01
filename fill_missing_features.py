import pandas as pd

# Path to your current CSV (35 features)
input_csv = "datasets/new_apks_features.csv"

# Load existing CSV
df = pd.read_csv(input_csv)

# List of all 470 feature columns (same as training)
columns_470 = [
    'ACCESS_PERSONAL_INFO___', 'ALTER_PHONE_STATE___', 'ANTI_DEBUG_____', 'CREATE_FOLDER_____', 
    'CREATE_PROCESS`_____', 'CREATE_THREAD_____', 'DEVICE_ACCESS_____', 'EXECUTE_____', 
    'FS_ACCESS____', 'FS_ACCESS()____', 'FS_ACCESS(CREATE)____', 'FS_ACCESS(CREATE__APPEND)__', 
    'FS_ACCESS(CREATE__READ)__', 'FS_ACCESS(CREATE__READ__WRITE)', 'FS_ACCESS(CREATE__WRITE)__', 
    'FS_ACCESS(CREATE__WRITE__APPEND)', 'FS_ACCESS(READ)____', 'FS_ACCESS(READ__WRITE)__', 
    'FS_ACCESS(WRITE)____', 'FS_PIPE_ACCESS___', 'FS_PIPE_ACCESS()___', 'FS_PIPE_ACCESS(READ)___', 
    'FS_PIPE_ACCESS(READ__)_', 'FS_PIPE_ACCESS(READ__WRITE)_', 'FS_PIPE_ACCESS(WRITE)___', 
    'NETWORK_ACCESS____', 'NETWORK_ACCESS()____', 'NETWORK_ACCESS(READ)____', 
    'NETWORK_ACCESS(READ__WRITE)__', 'NETWORK_ACCESS(READ__WRITE__)', 'NETWORK_ACCESS(WRITE)____', 
    'NETWORK_ACCESS(WRITE__)__', 'SMS_SEND____', 'TERMINATE_PROCESS', 'TERMINATE_THREAD',
    '__arm_nr_cacheflush', '__arm_nr_set_tls', '_llseek', '_newselect', 'accept', 'access', 
    'add', 'addAccessibilityInteractionConnection', 'addAccountExplicitly', 'addClient', 
    'addPeriodicSync', 'addStatusChangeListener', 'addToDisplay', 'addToDisplayWithoutInputChannel', 
    'addWithoutInputChannel', 'attachEngine', 'beginRestoreSession', 'bind', 'brk', 'cancelAllNotifications', 
    'cancelNotificationWithTag', 'cancelSync', 'cancelToast', 'cancelVibrate', 'capset', 'chdir', 
    'checkOperation', 'checkPackage', 'checkPermission', 'checkSignatures', 'chmod', 'chown32', 
    'clock_getres', 'clock_gettime', 'clone', 'close', 'collapsePanels', 'connect', 
    'currentToCanonicalPackageNames', 'dataChanged', 'deleteHost', 'disconnect', 'displayCompletions', 
    'dup', 'dup2', 'endRestoreSession', 'engineShown', 'enqueueNotificationWithTag', 'enqueueToast', 
    'epoll_create', 'epoll_ctl', 'epoll_wait', 'eventfd2', 'execve', 'exit', 'exit_group', 
    'faccessat', 'fchmod', 'fchown32', 'fcntl', 'fcntl64', 'fdatasync', 'finishDrawing', 
    'finishInput', 'finishSpellCheckerService', 'flock', 'fork', 'fstat64', 'fstatfs64', 
    'fsync', 'ftruncate', 'ftruncate64', 'futex', 'geocoderIsPresent', 'getAccounts', 
    'getAccountsAsUser', 'getActiveAdmins', 'getActiveNetworkInfo', 'getActivePhoneType', 
    'getActivityInfo', 'getAllCellInfo', 'getAllNetworkInfo', 'getAllPkgUsageStats', 'getAllProviders', 
    'getAnimationScale', 'getAppWidgetIds', 'getAppWidgetInfo', 'getApplicationEnabledSetting', 
    'getApplicationInfo', 'getApplicationRestrictions', 'getAuthenticatorTypes', 'getBestProvider', 
    'getBoolean', 'getCallState', 'getCameraDisabled', 'getCameraInfo', 'getCellLocation', 
    'getClientDefaultLanguage', 'getComponentEnabledSetting', 'getConfiguredNetworks', 'getConnectionInfo', 
    'getCurrentInputMethodSubtype', 'getCurrentModeType', 'getCurrentSpellChecker', 'getCurrentSpellCheckerSubtype', 
    'getDataActivity', 'getDataNetworkType', 'getDataState', 'getDeviceId', 'getDeviceList', 'getDeviceOwner', 
    'getDeviceSvn', 'getDhcpInfo', 'getDisplayFrame', 'getDisplayIds', 'getDisplayInfo', 
    'getEnabledAccessibilityServiceList', 'getEnabledInputMethodList', 'getEnabledInputMethodSubtypeList', 
    'getFlashlightEnabled', 'getFromLocation', 'getGlobalSearchActivity', 'getGroupIdLevel1', 'getHeightHint', 
    'getIccSerialNumber', 'getInTouchMode', 'getInputDevice', 'getInputDeviceIds', 'getInputMethodList', 
    'getInstallLocation', 'getInstalledApplications', 'getInstalledPackages', 'getInstalledProviders', 
    'getInstallerPackageName', 'getIsSyncable', 'getLastChosenActivity', 'getLastInputMethodSubtype', 
    'getLastLocation', 'getLine1Number', 'getLong', 'getMasterSyncAutomatically', 'getMessenger', 
    'getMobileDataEnabled', 'getMobileIfaces', 'getMode', 'getNameForUid', 'getNeighboringCellInfo', 
    'getNetworkInfo', 'getNetworkPreference', 'getNightMode', 'getNumberOfCameras', 'getPackageGids', 
    'getPackageInfo', 'getPackageSizeInfo', 'getPackagesForUid', 'getPassword', 'getPermissionGroupInfo', 
    'getPermissionInfo', 'getPreferredActivities', 'getPreferredPackages', 'getPrimaryClip', 'getProviderInfo', 
    'getProviderProperties', 'getProviders', 'getProxy', 'getReceiverInfo', 'getRingerMode', 'getRingtonePlayer', 
    'getScanResults', 'getSearchableInfo', 'getSearchablesInGlobalSearch', 'getServiceInfo', 'getSpellCheckerService', 
    'getState', 'getStorageEncryptionStatus', 'getStreamMaxVolume', 'getStreamVolume', 'getString', 
    'getSubscriberId', 'getSyncAutomatically', 'getSystemAvailableFeatures', 'getSystemSharedLibraryNames', 
    'getTetheredIfaces', 'getUserData', 'getUserIcon', 'getUserRestrictions', 'getUserSerialNumber', 'getUsers', 
    'getVibrateSetting', 'getVoiceMailAlphaTag', 'getVoiceMailNumber', 'getWallpaper', 'getWallpaperInfo', 
    'getWidthHint', 'getWifiApConfiguration', 'getWifiApEnabledState', 'getWifiDisplayStatus', 'getWifiEnabledState', 
    'getWifiServiceMessenger', 'getcwd', 'getdents64', 'getegid32', 'geteuid32', 'getgid32', 'getgroups32', 
    'getpeername', 'getpgid', 'getpid', 'getppid', 'getpriority', 'getresgid32', 'getresuid32', 'getrusage', 
    'getsockname', 'getsockopt', 'gettid', 'gettimeofday', 'getuid32', 'hasClipboardText', 'hasIccCard', 'hasKeys', 
    'hasNamedWallpaper', 'hasNavigationBar', 'hasPrimaryClip', 'hasSystemFeature', 'hasVibrator', 
    'hideSoftInput', 'inKeyguardRestrictedInputMode', 'inotify_add_watch', 'inotify_init', 'inotify_rm_watch', 
    'ioctl', 'isActiveNetworkMetered', 'isAdminActive', 'isBluetoothA2dpOn', 'isBluetoothScoOn', 'isCameraSoundForced', 
    'isImsSmsSupported', 'isKeyguardLocked', 'isKeyguardSecure', 'isPackageAvailable', 'isProviderEnabled', 
    'isSafeMode', 'isScanAlwaysAvailable', 'isScreenOn', 'isSpeakerphoneOn', 'isSpellCheckerEnabled', 'isSyncActive', 
    'isWakeLockLevelSupported', 'lgetxattr', 'link', 'listen', 'locationCallbackFinished', 'lseek', 'lstat64', 
    'madvise', 'mkdir', 'mknod', 'mlock', 'mmap2', 'mount', 'mprotect', 'mremap', 'msync', 'munlock', 'munmap', 
    'nanosleep', 'notifyAppWidgetViewDataChanged', 'notifyChange', 'onChange', 'onClose', 'onFinished', 
    'onGetSentenceSuggestionsMultiple', 'onRectangleOnScreenRequested', 'onRequestContinued', 'onResult', 'open', 
    'openSession', 'partiallyUpdateAppWidgetIds', 'performDeferredDestroy', 'pingSupplicant', 'pipe', 'pipe2', 
    'play', 'playSoundEffect', 'playSoundEffectVolume', 'poll', 'prctl', 'pread64', 'prepareVpn', 'ptrace', 
    'pwrite64', 'queryContentProviders', 'queryIntentActivities', 'queryIntentContentProviders', 'queryIntentReceivers', 
    'queryIntentServices', 'read', 'readlink', 'reassociate', 'recvfrom', 'recvmsg', 'reenableKeyguard', 'registerCallback', 
    'registerContentObserver', 'registerInputDevicesChangedListener', 'registerMediaButtonIntent', 
    'registerRemoteControlClient', 'registerSuggestionSpansForNotification', 'relayout', 'releaseMulticastLock', 
    'releaseWakeLock', 'releaseWifiLock', 'remove', 'removeAccessibilityInteractionConnection', 'removeActiveAdmin', 
    'removeGpsStatusListener', 'removePrimaryClipChangedListener', 'removeStatusChangeListener', 'rename', 
    'requestLocationUpdates', 'requestScanFile', 'resolveContentProvider', 'resolveIntent', 'resolveService', 
    'restorePackage', 'rmdir', 'rt_sigprocmask', 'rt_sigtimedwait', 'sched_get_priority_max', 'sched_get_priority_min', 
    'sched_getparam', 'sched_getscheduler', 'sched_setscheduler', 'sched_setscheduler', 'sched_yield', 'send', 
    'sendAccessibilityEvent', 'sendExtraCommand', 'sendMultipartText', 'sendText', 'sendmsg', 'sendto', 'set', 
    'setActivityWatcher', 'setAlarm', 'setAlwaysFinish', 'setApplicationBlocked', 'setApplicationHiddenSettingAsUser', 
    'setAutoFillService', 'setAutoRestartDisabled', 'setBluetoothA2dpOn', 'setBluetoothScoOn', 
    'setCameraDisabled', 'setComponentEnabledSetting', 'setDataRoamingEnabled', 'setDeviceOwner', 
    'setDns', 'setDisplayHomeAsUpEnabled', 'setGlobalSetting', 'setInputMethodEnabled', 'setInputMethodEnabledFromSubtype', 
    'setInputMethodSelectorVisibility', 'setInstallLocation', 'setKeyguardDisabled', 'setMasterSyncAutomatically', 
    'setNetworkPreference', 'setPackageStoppedState', 'setPersistent', 'setRingerMode', 'setRotation', 'setStreamVolume', 
    'setText', 'setTime', 'setTimeZone', 'setUserIcon', 'setUserRestriction', 'setUserRestrictions', 'setVolume', 
    'setWifiApEnabled', 'setWindowFlags', 'setXAttr', 'shutdown', 'sigaction', 'sigaltstack', 'sign', 'socket', 
    'socketpair', 'splice', 'stat64', 'statfs64', 'statvfs', 'stopAppSwitches', 'stopInput', 'stopInputMethod', 
    'stopSearch', 'symlink', 'sync', 'syncInput', 'syscall', 'syslog', 'systemProperties', 'tcgetattr', 'tcsetattr', 
    'tee', 'tgkill', 'time', 'timer_create', 'timer_delete', 'timer_getoverrun', 'timer_gettime', 'timer_settime', 
    'timerfd_create', 'timerfd_gettime', 'timerfd_settime', 'tkill', 'truncate', 'umount', 'uname', 'unlink', 
    'unlinkat', 'utime', 'utimensat', 'utimes', 'vfork', 'vmsplice', 'vserver', 'wait4', 'waitpid', 'write'
]

# Add missing columns with default value 0
for col in columns_470:
    if col not in df.columns:
        df[col] = 0

# Reorder columns as in training
df = df[columns_470]

# Save CSV (overwrite existing)
df.to_csv("datasets/new_apks_features.csv", index=False)

print("✅ CSV updated with 470 features! Tum ab predict_apk.py run kar sakte ho.")
