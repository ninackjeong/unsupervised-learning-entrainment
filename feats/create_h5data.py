from entrainment_config import *

SEED=448
frac_train = 0.8
frac_val = 0.1

# Create h5 files

data_dir = data_dir


sessList= sorted(glob.glob(data_dir + '*.csv'))
random.seed(SEED)
random.shuffle(sessList)

num_files_all = len(sessList)
num_files_train = int(np.ceil((frac_train*num_files_all)))
num_files_val = int(np.ceil((frac_val*num_files_all)))
num_files_test = num_files_all - num_files_train - num_files_val

sessTrain = sessList[:num_files_train]
sessVal = sessList[num_files_train:num_files_val+num_files_train]
sessTest = sessList[num_files_val+num_files_train:]
print(len(sessTrain) + len(sessVal) + len(sessTest))

# Create Train Data file

X_train =np.array([])
X_train = np.empty(shape=(0, 0), dtype='float64' )
for sess_file in sessTrain:
	df_i = pd.read_csv(sess_file)
	xx=np.array(df_i)
	X_train=np.vstack([X_train, xx]) if X_train.size else xx


X_train = X_train.astype('float64')
hf = h5py.File('data/train_Fisher_nonorm.h5', 'w')
hf.create_dataset('dataset', data=X_train)
hf.create_dataset('prosset', data=X_train[:,:24])
hf.create_dataset('specset', data=X_train[:,24:150])
hf.create_dataset('vqset', data=X_train[:,150:])
hf.close()


# Create Val Data file

X_val =np.array([])
for sess_file in sessVal:
	df_i = pd.read_csv(sess_file)
	xx=np.array(df_i)
	X_val=np.vstack([X_val, xx]) if X_val.size else xx

X_val = X_val.astype('float64')
hf = h5py.File('data/val_Fisher_nonorm.h5', 'w')
hf.create_dataset('dataset', data=X_val)
hf.create_dataset('prosset', data=X_val[:,:24])
hf.create_dataset('specset', data=X_val[:,24:150])
hf.create_dataset('vqset', data=X_val[:,150:])
hf.close()




# Create Test Data file
spk_base = 1
X_test =np.array([])
for sess_file in sessTest:
	df_i = pd.read_csv(sess_file)
	xx=np.array(df_i)
	N = xx.shape[0]
	if np.mod(N,2)==0:
		spk_label = np.tile([spk_base, spk_base+1], [1, N/2])
	else:
		spk_label = np.tile([spk_base, spk_base+1], [1, N/2])
		spk_label = np.append(spk_label, spk_base)
	xx = np.hstack((xx, spk_label.T.reshape([N,1])))
	X_test=np.vstack([X_test, xx]) if X_test.size else xx
	spk_base += 1


X_test = X_test.astype('float64')
hf = h5py.File('data/test_Fisher_nonorm.h5', 'w')
hf.create_dataset('dataset', data=X_test)
hf.create_dataset('prosset', data=X_test[:,:24])
hf.create_dataset('specset', data=X_test[:,24:150])
hf.create_dataset('vqset', data=X_test[:,150:])
hf.close()




data_dir = data_dir

sessList= sorted(glob.glob(data_dir + '*.csv'))
random.seed(SEED)
random.shuffle(sessList)

num_files_all = len(sessList)
num_files_train = int(np.ceil((frac_train*num_files_all)))
num_files_val = int(np.ceil((frac_val*num_files_all)))
num_files_test = num_files_all - num_files_train - num_files_val

sessTrain = sessList[:num_files_train]
sessVal = sessList[num_files_train:num_files_val+num_files_train]
sessTest = sessList[num_files_val+num_files_train:]
print(len(sessTrain) + len(sessVal) + len(sessTest))

# Create Train Data file

X_train =np.array([])
X_train = np.empty(shape=(0, 0), dtype='float64' )
for sess_file in sessTrain:
	df_i = pd.read_csv(sess_file)
	xx=np.array(df_i)
	X_train=np.vstack([X_train, xx]) if X_train.size else xx


X_train = X_train.astype('float64')
hf = h5py.File('data/train_Fisher_nonorm_nopre.h5', 'w')
hf.create_dataset('dataset', data=X_train)
hf.create_dataset('prosset', data=X_train[:,:24])
hf.create_dataset('specset', data=X_train[:,24:150])
hf.create_dataset('vqset', data=X_train[:,150:])
hf.close()


# Create Val Data file

X_val =np.array([])
for sess_file in sessVal:
	df_i = pd.read_csv(sess_file)
	xx=np.array(df_i)
	X_val=np.vstack([X_val, xx]) if X_val.size else xx

X_val = X_val.astype('float64')
hf = h5py.File('data/val_Fisher_nonorm_nopre.h5', 'w')
hf.create_dataset('dataset', data=X_val)
hf.create_dataset('prosset', data=X_val[:,:24])
hf.create_dataset('specset', data=X_val[:,24:150])
hf.create_dataset('vqset', data=X_val[:,150:])
hf.close()




# Create Test Data file
spk_base = 1
X_test =np.array([])
for sess_file in sessTest:
	df_i = pd.read_csv(sess_file)
	xx=np.array(df_i)
	N = xx.shape[0]
	if np.mod(N,2)==0:
		spk_label = np.tile([spk_base, spk_base+1], [1, N/2])
	else:
		spk_label = np.tile([spk_base, spk_base+1], [1, N/2])
		spk_label = np.append(spk_label, spk_base)
	xx = np.hstack((xx, spk_label.T.reshape([N,1])))
	X_test=np.vstack([X_test, xx]) if X_test.size else xx
	spk_base += 1


X_test = X_test.astype('float64')
hf = h5py.File('data/test_Fisher_nonorm_nopre.h5', 'w')
hf.create_dataset('dataset', data=X_test)
hf.create_dataset('prosset', data=X_test[:,:24])
hf.create_dataset('specset', data=X_test[:,24:150])
hf.create_dataset('vqset', data=X_test[:,150:])
hf.close()



