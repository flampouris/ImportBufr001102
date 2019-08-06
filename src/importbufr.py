def read_001002(WAVstr, filename):

    import ncepbufr
    import numpy as np
    from datetime import datetime

    dtstr='YEAR MNTH DAYS HOUR MINU'
    lcstr='CLONH CLATH'

    bufr = ncepbufr.open(filename)

    #bufr.dump_table('prepbufr.table')

    cnt = 0
    datestmp = []   #[YYYY MM DD HH]
    loc = []        #[lon lat]
    wav = []

    while bufr.advance() == 0: # loop over messages.
    #    print(bufr.msg_counter, bufr.msg_type, bufr.msg_date, bufr.receipt_time)
        while bufr.load_subset() == 0: # loop over subsets in message.
            #bufr.dump_subset('xx102.dumped',append=True)
            wavdum = bufr.read_subset(WAVstr).squeeze()
            #wavdum = bufr.read_subset(SSTstr, seq=True).squeeze()-273.15
            if np.isfinite(wavdum).any():
                wav=np.append(wav, wavdum)
                datestmp = np.append (datestmp, bufr.read_subset(dtstr).squeeze(), axis=0)

                loc = np.append ( loc, bufr.read_subset(lcstr).squeeze() )
                cnt += 1
                print(cnt,' Observations are imported', 'np.shape(wav) = ', np.shape(wav), wavdum)
        #if bufr.msg_counter == 200 : break
    bufr.close()

    loc = np.reshape(loc, (cnt, int(np.array(np.shape(loc))/cnt)))

    wav = np.reshape(wav, (cnt, int(np.array(np.shape(wav))/cnt)))
    datestmp = np.reshape(datestmp, (cnt, int(np.array(np.shape(datestmp))/cnt)))

    d = dict()
    d['longitude'] = loc[:,0]
    d['latitude'] = loc[:,1]
    cnt=0
    for i in WAVstr.split(' '):
        d[i] = wav[:,cnt]
        cnt+=1
    d['date']=[]
    for i in range(len(datestmp)):
        d['date'].append(datetime(year=int(datestmp[i,0]),month=int(datestmp[i,1]),day=int(datestmp[i,2]),hour=int(datestmp[i,3]),minute=int(datestmp[i,4])))
    return d

