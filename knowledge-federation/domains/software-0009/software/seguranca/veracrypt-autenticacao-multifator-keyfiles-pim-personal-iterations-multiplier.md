---
id: software.seguranca.tranche08.000714
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/veracrypt/VeraCrypt/master/README.md", "https://veracrypt.io/en/Command%20Line%20Usage.html", "https://veracrypt.io/en/Documentation.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# VeraCrypt: Autenticação Multifator de Volumes com **Keyfiles**, Tokens PKCS#11 (YubiKey/SmartCard) e **PIM (*Personal Iterations Multiplier*)**

## Em uma frase
Para proteger volumes críticos contra captura de teclado (*keyloggers*) ou vazamento de senha, o VeraCrypt combina três fatores independentes na derivação da chave do cabeçalho: **(1) Passphrase**, **(2) Um ou mais Keyfiles** (arquivos arbitrários ou objetos armazenados em um token de hardware **PKCS#11**) e **(3) PIM (*Personal Iterations Multiplier*)**.

## Por que importa
Diferente de um arquivo de chave fixo que substitui a senha, no VeraCrypt os **Keyfiles são misturados criptograficamente com a senha**: o VeraCrypt lê os primeiros 1 MiB de cada arquivo selecionado (ou todos os arquivos de uma pasta) e aplica um acumulador CRC-32/Whirlpool sobre o pool de senha antes de alimentar o PBKDF2, de modo que **a ordem dos keyfiles não importa, mas a falta ou alteração de um único bit em qualquer keyfile impede totalmente a derivação da chave**!

## Como funciona
Já o **PIM** permite ao usuário definir uma fórmula customizada de iterações PBKDF2 (`Iterações = 15000 + (PIM * 1000)` para volumes normais com SHA-512/Whirlpool): um atacante que roda o Hashcat (`-m 13721`) sem conhecer o número PIM customizado sequer sabe quantas iterações de PBKDF2 precisa calcular por tentativa!

## Exemplo
```bash
# Gerar um keyfile de 64 bytes com entropia criptografica pura do kernel e montar o volume combinando senha + keyfile + PIM
head -c 64 /dev/urandom > /etc/secops/keys/vc_token.keyfile
chmod 0400 /etc/secops/keys/vc_token.keyfile

veracrypt --text --mount /cases/vaults/dfir_evidence.hc /mnt/evidence \
  --hash=sha512 --pim=485 \
  --keyfiles=/etc/secops/keys/vc_token.keyfile \
  --protect-hidden=no --non-interactive --stdin <<< "Passphrase-Forte-2026!"
```

## Limites e trade-offs
Nunca escolha como *Keyfile* um arquivo estático cujo conteúdo possa ser modificado por aplicativos no dia a dia (como um documento `.docx` editável ou banco SQLite), pois se qualquer programa alterar 1 byte do arquivo você perderá o acesso ao volume; use um arquivo dedicado somente-leitura (`--generate-keyfile`) guardado em um token de hardware PKCS#11.

## Como verificar
Gere keyfiles com `veracrypt --text --create-keyfile /caminho/keyfile` e mantenha backup seguro fora do host.

## Conexões
- [[veracrypt-cifras-cascata-aes-twofish-serpent-camellia-kuznyechik]] — Veja também: VeraCrypt: Cifras Individuais vs **Cifras em Cascata (*Cascades*: `AES-Twofish-Serpent`)** em Modo XTS e Impacto de Hardware `AES-NI`.
- [[veracrypt-volumes-ocultos-hidden-volumes-plausible-deniability-protecao]] — Veja também: VeraCrypt: **Hidden Volumes (*Plausible Deniability*)**, Funcionamento da Proteção de Volume Oculto (`--protect-hidden`) e Limites Forenses.
- [[veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho]] — Referência cruzada direta com veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho.
- [[veracrypt-criacao-montagem-cli-headless-non-interactive-linux]] — Referência cruzada direta com veracrypt-criacao-montagem-cli-headless-non-interactive-linux.
- [[hashcat-mapeamento-teclado-hex-salt-compressao-arquivos-fde]] — Referência cruzada direta com hashcat-mapeamento-teclado-hex-salt-compressao-arquivos-fde.

## Fontes
- [VeraCrypt Official GitHub Repository — Architecture & Reproducible Builds](https://raw.githubusercontent.com/veracrypt/VeraCrypt/master/README.md) — repositório oficial do VeraCrypt (IDRIX) cobrindo arquitetura criptográfica, builds reprodutíveis e verificação de assinaturas; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Command Line Usage Reference](https://veracrypt.io/en/Command%20Line%20Usage.html) — documentação oficial de linha de comando do VeraCrypt cobrindo criação, montagem, PIM, keyfiles e volumes ocultos; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Technical & Security Guide](https://veracrypt.io/en/Documentation.html) — guia técnico oficial do VeraCrypt sobre modo XTS, cifras em cascata, cabeçalho de backup e proteção de memória; consultado em 2026-10-03.
