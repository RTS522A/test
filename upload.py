import sys
import time
import libtorrent as lt

#Create torrent
fs = lt.file_storage()
lt.add_files(fs, "./wimlib.zip")
t = lt.create_torrent(fs)
t.add_tracker("http://denis.stalker.h3q.com:6969/announce")
t.add_tracker("")
t.add_tracker("udp://tracker.leechers-paradise.org:6969")
t.add_tracker("")
t.add_tracker("http://tracker.openbittorrent.com/announce")
t.add_tracker("")
t.add_tracker("http://tracker.istole.it:80/announce")
t.add_tracker("")
t.add_tracker("http://papaja.v2v.cc:6970/announce")
t.add_tracker("")
t.add_tracker("http://bt.nnm-club.info:2710/announce")
t.add_tracker("")
t.add_tracker("http://sound-park.ru/announce.php")
t.add_tracker("")
t.add_tracker("udp://tracker.trackerfix.com:83/announce")
t.add_tracker("")
t.add_tracker("udp://tracker.opentrackr.org:1337/announce")
t.add_tracker("")
t.add_tracker("udp://tracker.ilibr.org:6969/announce")
t.add_tracker("")
t.add_tracker("udp://shadowshq.yi.org:6969/announce")
t.add_tracker("")
t.add_tracker("http://retracker.local/announce")
t.add_tracker("")
t.add_tracker("http://210.244.71.25:6969/announce")
t.add_tracker("")
t.set_creator('libtorrent %s' % lt.version)
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()    
f = open("mytorrent.torrent", "wb")
f.write(lt.bencode(torrent))
f.close()

#Seed torrent
ses = lt.session({'listen_interfaces': '0.0.0.0:6881'})

info = lt.torrent_info("mytorrent.torrent")
h = ses.add_torrent({'ti': info, 'save_path': '.'})
s = h.status()
print('starting', s.name)

while (True):
    s = h.status()

    print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
        s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
        s.num_peers, s.state), end=' ')

#    alerts = ses.pop_alerts()
#    for a in alerts:
#        if a.category() & lt.alert.category_t.error_notification:
#            print(a)

    sys.stdout.flush()

    time.sleep(10)

print(h.status().name, 'complete')
