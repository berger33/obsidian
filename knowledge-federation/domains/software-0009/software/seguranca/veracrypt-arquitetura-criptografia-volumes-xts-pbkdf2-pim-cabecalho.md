---
id: software.seguranca.tranche08.000711
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

# VeraCrypt: Arquitetura de Criptografia de Volumes Multiplataforma, Modo **XTS (IEEE P1619)**, **PBKDF2-RIPEMD160/SHA-512/Whirlpool/BLAKE2s** e **PIM**

## Em uma frase
**VeraCrypt** (`veracrypt/VeraCrypt`, mantido pela IDRIX / Mounir Idrassi) é a solução open-source multiplataforma (Windows, Linux, macOS, FreeBSD, OpenBSD) para criptografia em tempo real (*on-the-fly*) de arquivos-contêiner, partições e discos de sistema completos, nascida como evolução auditada do TrueCrypt 7.1a.

## Por que importa
Para corrigir a baixa contagem de iterações de derivação de chave do antigo TrueCrypt (que usava apenas 1.000 ou 2.000 iterações de PBKDF2), o VeraCrypt aumentou drasticamente o fator de trabalho padrão (**500.000 iterações** para SHA-512/Whirlpool/BLAKE2s em partições não-sistema, e **200.000+** para boot) e introduziu o parâmetro **PIM (*Personal Iterations Multiplier*)**.

## Como funciona
No nível de bloco, todo volume VeraCrypt é indistinguível de dados 100% aleatórios (sem assinatura mágica ou cabeçalho em texto claro no disco!): os primeiros 64 KiB contêm o cabeçalho cifrado em modo **XTS (IEEE P1619)** com duas chaves independentes de 256 bits (512 bits totais para XTS-AES-256), mais uma cópia de backup do cabeçalho embutida nos últimos 64 KiB do volume.

## Exemplo
```bash
# Exibir a versao e as opcoes do modo texto/console (--text / -t) do VeraCrypt em sistemas Linux/Unix
veracrypt --text --version
veracrypt --text --help | head -n 30
```

## Limites e trade-offs
Como um volume VeraCrypt não possui cabeçalho identificável em texto claro no disco, quando você monta um volume sem especificar o algoritmo de hash (`--hash`), o VeraCrypt precisa testar sequencialmente todos os KDFs suportados (SHA-512, Whirlpool, SHA-256, BLAKE2s, Streebog), o que leva alguns segundos extras; especificar `--hash sha512` na montagem torna o desbloqueio instantâneo!

## Como verificar
Verifique os volumes montados no terminal executando **`veracrypt --text --list`**.

## Conexões
- [[veracrypt-criacao-montagem-cli-headless-non-interactive-linux]] — Veja também: VeraCrypt em Servidores Linux Headless (`veracrypt --text --non-interactive`): Criação, Montagem Segura via `stdin` e Desmontagem.
- [[veracrypt-cifras-cascata-aes-twofish-serpent-camellia-kuznyechik]] — Referência cruzada direta com veracrypt-cifras-cascata-aes-twofish-serpent-camellia-kuznyechik.
- [[cryptsetup-abertura-volumes-bitlocker-veracrypt-truecrypt-forense]] — Referência cruzada direta com cryptsetup-abertura-volumes-bitlocker-veracrypt-truecrypt-forense.

## Fontes
- [VeraCrypt Official GitHub Repository — Architecture & Reproducible Builds](https://raw.githubusercontent.com/veracrypt/VeraCrypt/master/README.md) — repositório oficial do VeraCrypt (IDRIX) cobrindo arquitetura criptográfica, builds reprodutíveis e verificação de assinaturas; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Command Line Usage Reference](https://veracrypt.io/en/Command%20Line%20Usage.html) — documentação oficial de linha de comando do VeraCrypt cobrindo criação, montagem, PIM, keyfiles e volumes ocultos; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Technical & Security Guide](https://veracrypt.io/en/Documentation.html) — guia técnico oficial do VeraCrypt sobre modo XTS, cifras em cascata, cabeçalho de backup e proteção de memória; consultado em 2026-10-03.
