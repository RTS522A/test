import sys
import time
import libtorrent as lt

#Create torrent
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.openbittorrent.com:80/announce\n")
t.add_tracker("udp://denis.stalker.h3q.com:6969/announce\n")
t.add_tracker("http://denis.stalker.h3q.com:6969/announce\n")
t.add_tracker("udp://open.demonii.com:1337\n")
t.add_tracker("udp://tracker.coppersurfer.tk:6969\n")
t.add_tracker("udp://tracker.leechers-paradise.org:6969\n")
t.add_tracker("http://tracker.openbittorrent.com/announce\n")
t.add_tracker("udp://tracker.openbittorrent.com:80/announce\n")
t.add_tracker("http://tracker.torrentbay.to:6969/announce\n")
t.add_tracker("http://tracker.istole.it:80/announce\n")
t.add_tracker("http://tracker.torrent.to:2710/announce\n")
t.add_tracker("http://papaja.v2v.cc:6970/announce\n")
t.add_tracker("udp://tracker.publicbt.com:80/announce\n")
t.add_tracker("http://tracker3.torrentino.com/announce?passkey=00000000000000000000000000000000\n")
t.add_tracker("http://bt.nnm-club.ru:2710/announce\n")
t.add_tracker("http://bt.nnm-club.info:2710/announce\n")
t.add_tracker("http://www.filebase.ws:5678/announce\n")
t.add_tracker("http://exodus.desync.com/announce\n")
t.add_tracker("http://www.progressivetorrents.com/announce.php\n")
t.add_tracker("http://retracker.bashtel.ru/announce.php\n")
t.add_tracker("http://piratbit.net/bt/announce.php\n")
t.add_tracker("http://sound-park.ru/announce.php\n")
t.add_tracker("udp://tracker.trackerfix.com:83/announce\n")
t.add_tracker("udp://tracker.opentrackr.org:1337/announce\n")
t.add_tracker("udp://tracker.zer0day.to:1337/announce\n")
t.add_tracker("udp://explodie.org:6969/announce\n")
t.add_tracker("udp://eddie4.nl:6969/announce\n")
t.add_tracker("udp://tracker.ilibr.org:6969/announce\n")
t.add_tracker("udp://shadowshq.yi.org:6969/announce\n")
t.add_tracker("udp://shubt.net:2710\n")
t.add_tracker("http://retracker.local/announce\n")
t.add_tracker("http://tracker.filetracker.pl:8089/announce\n")
t.add_tracker("http://tracker2.wasabii.com.tw:6969/announce\n")
t.add_tracker("http://tracker.grepler.com:6969/announce\n")
t.add_tracker("http://80.246.243.18:6969/announce\n")
t.add_tracker("http://125.227.35.196:6969/announce\n")
t.add_tracker("http://tracker.tiny-vps.com:6969/announce\n")
t.add_tracker("http://87.248.186.252:8080/announce\n")
t.add_tracker("http://www.torrentheaven.de/announce.php\n")
t.add_tracker("http://tracker.mp3-es.com/announce.php\n")
t.add_tracker("http://210.244.71.25:6969/announce\n")
t.add_tracker("http://46.4.109.148:6969/announce\n")
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

while (not s.is_seeding):
    s = h.status()

    print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
        s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
        s.num_peers, s.state), end=' ')

    alerts = ses.pop_alerts()
    for a in alerts:
        if a.category() & lt.alert.category_t.error_notification:
            print(a)

    sys.stdout.flush()

    time.sleep(10)

print(h.status().name, 'complete')
