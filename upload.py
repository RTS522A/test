import libtorrent as lt
import sys, time


videoFile = "test.txt"
workingPath = "."

#Create torrent

f = lt.file_storage()
lt.add_files(f, videoFile)
t = lt.create_torrent(f)
t.add_node("router.utorrent.com", 6881)
t.add_node("dht.transmissionbt.com", 6881)
lt.set_piece_hashes(t, workingPath)
torrent = t.generate()
f = open("1.torrent", "wb")
f.write(lt.bencode(torrent))
f.close()

#Seeding

PORT_RANGE = (6881,6891)
s = lt.session()
s.listen_on(PORT_RANGE[0],PORT_RANGE[1])
s.add_dht_router('router.utorrent.com',6881)
s.start_dht()
print("DHT start: ", s.is_dht_running())
print("DHT state: ", s.dht_state())


params = {
            'save_path': workingPath,
            'storage_mode': lt.storage_mode_t.storage_mode_sparse,
            'ti': lt.torrent_info(torrent),
            'seed_mode': True,
            'paused': False,
            'upload_mode':True,
            'super_seeding':True
        }
h = s.add_torrent(params)
print("Total size: " + str(h.status().total_wanted))
print("Name: " + h.name())
while True:
    s = h.status()
    msg = '\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s'
    print(msg % (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, s.state))
    sys.stdout.flush()
    time.sleep(1)
