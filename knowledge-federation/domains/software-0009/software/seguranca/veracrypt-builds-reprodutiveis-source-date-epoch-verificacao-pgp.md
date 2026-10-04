---
id: software.seguranca.tranche08.000720
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

# VeraCrypt: Verificação de Supply Chain — Assinaturas OpenPGP da IDRIX e **Builds Reprodutíveis (`SOURCE_DATE_EPOCH`)** para `.deb` e `.rpm`

## Em uma frase
Como um software de criptografia de disco tem acesso direto à chave mestra e a todos os arquivos em texto claro, um binário adulterado do VeraCrypt comprometeria totalmente a segurança; por isso, o projeto VeraCrypt publica assinaturas OpenPGP para todos os instaladores e suporta **Builds Reprodutíveis (*Reproducible Builds*)**.

## Por que importa
Conforme documentado no `README.md` oficial do repositório `veracrypt/VeraCrypt`, tanto os pacotes `.deb` quanto `.rpm` gerados a partir do código-fonte são **determinísticos e reprodutíveis** (usando a variável **`SOURCE_DATE_EPOCH`** ou a data de release em `src/Common/Tcdefs.h` às `00:00 UTC`), permitindo que auditores independentes compilem o código-fonte do GitHub e obtenham um binário bit-a-bit idêntico ao distribuído oficialmente.

## Como funciona
No Windows, conforme explica o `README.md`, os executáveis `.exe` e drivers `.sys` oficiais contêm a cadeia de assinatura digital Authenticode da IDRIX/GlobalSign anexada ao final do binário PE.

## Exemplo
```bash
# Compilar o executavel console-only (NOGUI=1) do VeraCrypt no Linux de forma reprodutivel com SOURCE_DATE_EPOCH
gpgv --keyring /etc/secops/keyrings/idrix-veracrypt.gpg VeraCrypt-1.26.20-Setup.tar.bz2.sig VeraCrypt-1.26.20-Setup.tar.bz2
```

## Limites e trade-offs
Ao instalar o VeraCrypt em estações de trabalho de segurança ou servidores de custódia de chaves, nunca baixe binários de sites espelho não-oficiais sem antes validar a assinatura `.sig` com `gpgv` contra o fingerprint oficial da chave pública do projeto VeraCrypt (`5069A233D55A0EEB174A5FC3821ACD02680D16DE`).

## Como verificar
Compare o hash SHA-256 do instalador baixado com o arquivo `sha256sum.txt` assinado pelo mantenedor.

## Conexões
- [[veracrypt-interoperabilidade-nativa-linux-cryptsetup-tcrypt-open]] — Veja também: Interoperabilidade Forense e Operacional: Abertura Nativa de Volumes **VeraCrypt** no Kernel Linux via **`cryptsetup open --type tcrypt --veracrypt`**.
- [[veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho]] — Referência cruzada direta com veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho.
- [[gnupg-verificacao-assinaturas-pacotes-gpgv-status-fd-automacao]] — Referência cruzada direta com gnupg-verificacao-assinaturas-pacotes-gpgv-status-fd-automacao.

## Fontes
- [VeraCrypt Official GitHub Repository — Architecture & Reproducible Builds](https://raw.githubusercontent.com/veracrypt/VeraCrypt/master/README.md) — repositório oficial do VeraCrypt (IDRIX) cobrindo arquitetura criptográfica, builds reprodutíveis e verificação de assinaturas; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Command Line Usage Reference](https://veracrypt.io/en/Command%20Line%20Usage.html) — documentação oficial de linha de comando do VeraCrypt cobrindo criação, montagem, PIM, keyfiles e volumes ocultos; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Technical & Security Guide](https://veracrypt.io/en/Documentation.html) — guia técnico oficial do VeraCrypt sobre modo XTS, cifras em cascata, cabeçalho de backup e proteção de memória; consultado em 2026-10-03.
