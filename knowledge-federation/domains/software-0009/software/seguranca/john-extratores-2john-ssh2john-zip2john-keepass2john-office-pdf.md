---
id: software.seguranca.tranche15.001455
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/README.md", "https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MODES"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# A Suíte de Extratores **`*2john`** do John Jumbo: Auditando Chaves Privadas SSH (`ssh2john`), Cofres (`keepass2john`), Arquivos `.zip`/`.7z`/`.rar` e Documentos Office/PDF

## Em uma frase
Durante um exercício de Red Team, Pentest ou perícia forense (DFIR), você encontra um arquivo **`id_rsa` / `id_ed25519` protegido por passphrase**, um arquivo compactado **`.zip` / `.7z` / `.rar` criptografado**, uma planilha **Excel/Word (`.xlsx`/`.docx`)**, um **PDF protegido** ou um cofre **KeePass (`.kdbx`)**. Por que você não passa um arquivo `.zip` ou `.pdf` de 500 MB diretamente para o `john`?

## Por que importa
Porque para testar 1 milhão de senhas por segundo, o motor criptográfico não precisa dos 500 MB do arquivo inteiro: ele precisa **apenas dos poucos bytes de cabeçalho criptográfico (`Salt`, `IV`, `Iterações KDF` e `Verifier Tag / Checkbytes`)**!

## Como funciona
É exatamente isso que os mais de **100 utilitários `*2john`** incluídos no diretório `run/` do John Jumbo fazem: eles parseiam o formato do arquivo binário e extraem uma única linha compacta de texto (`nome_arquivo:$formato$salt$iv$verifier`) pronta para ser auditada pelo `john`!

## Exemplo
```bash
# Extrair os cabecalhos criptograficos de uma chave privada SSH, de um arquivo ZIP cifrado e de um cofre KeePass usando os utilitarios *2john
ssh2john ./id_ed25519_protegida > ./hash_ssh.txt
zip2john ./backup_confidencial.zip > ./hash_zip.txt
keepass2john ./cofre_antigo.kdbx > ./hash_keepass.txt
john --wordlist=./dicionario.txt --rules=best64 ./hash_ssh.txt ./hash_zip.txt ./hash_keepass.txt
```

## Limites e trade-offs
Por que uma chave privada SSH antiga no formato PEM (`-----BEGIN RSA PRIVATE KEY-----` com `DEK-Info: AES-128-CBC`) é quebrada pelo `ssh2john` + `john` em milhões de tentativas por segundo, enquanto uma chave gerada no novo formato OpenSSH (**`ssh-keygen -o -a 100`**, `-----BEGIN OPENSSH PRIVATE KEY-----`) resiste bravamente? Porque o formato PEM legado derivava a chave usando apenas 1 rodada de `MD5` (`EVP_BytesToKey`), enquanto o formato OpenSSH moderno usa **`bcrypt_pbkdf` com dezenas ou centenas de rodadas (`-a 100`)**!

## Como verificar
Em arquivos `.zip`, use sempre criptografia **AES-256 (`7z a -tzip -mem=AES256`)** ou cifre com **`age` / `GPG`**, evitando o algoritmo legado *ZipCrypto (PKZIP stream cipher)* que é vulnerável a ataques de texto claro conhecido!

## Conexões
- [[john-modo-wordlist-regras-mangling-rules-best64-korelogic-custom]] — Veja também: Modo **`Wordlist` (`--wordlist`)** e Motor de **Regras de Mutação (`--rules` / `doc/RULES`)** no John the Ripper: `best64`, `KoreLogic`, `Jumbo` e Sintaxe de Regras.
- [[john-modos-incremental-markov-mask-subsets-entropia-baixa]] — Veja também: Modos Avançados Sem Dicionário no John the Ripper: **`Incremental` (Frequência de Trigramas `.chr`)**, **`Markov`**, **`Mask` (`?u?l?l?l?d?d?d?s`)** e **`Subsets`**.
- [[john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes]] — Referência cruzada direta com john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes.
- [[keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256]] — Referência cruzada direta com keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256.

## Fontes
- [John the Ripper Jumbo Official GitHub Repository (`openwall/john`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/README.md) — repositório oficial do Openwall John the Ripper Jumbo cobrindo mais de 400 formatos de hash/arquivos cifrados, aceleração SIMD/OpenCL e utilitários `*2john`; consultado em 2026-10-03.
- [John the Ripper Official Cracking Modes Specification (`doc/MODES`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MODES) — especificação oficial dos modos de ataque do John the Ripper detalhando `Single Crack` (GECOS), `Wordlist` com regras de mangling, `Incremental` (cadeias de Markov) e `External`; consultado em 2026-10-03.
