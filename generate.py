import zlib
import torch
import pickle
import io
FILENAME = 'test.p'
latents = torch.load('image1.pt')
y = torch.load('image_y.pt')
latent_hyp = pickle.load(open('latent_hyp.p', 'rb'))
# print(torch.all(torch.eq(y, latent_hyp)))
# print(latents, latents.size())
# print(y, y.size())

buffer = io.BytesIO()
torch.save(latents, buffer)

# new = torch.load(FILENAME)
# print(new)
# a = latents.byte
# h = pickle.dump(a, open(FILENAME, 'wb'))

# n = pickle.load(open(FILENAME, 'rb'))
# print(n)
compressed = zlib.compress(buffer.getvalue(), level=9)
pickle.dump(compressed, open(FILENAME, 'wb'))
