---
id: software.seguranca.tranche08.000712
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

# VeraCrypt em Servidores Linux Headless (`veracrypt --text --non-interactive`): Criação, Montagem Segura via `stdin` e Desmontagem

## Em uma frase
Em servidores Linux sem interface gráfica (`NOGUI=1` ou usando a flag **`--text`** / **`-t`**), o VeraCrypt permite criar e montar contêineres criptografados portáveis (para transporte seguro de evidências forenses DFIR, dumps de banco de dados ou chaves de backup) de forma 100% automatizada via CLI.

## Por que importa
Um erro grave de segurança ao montar volumes em linha de comando é passar a senha diretamente em `-p "MinhaSenha"` nos argumentos do comando: qualquer usuário local rodando `ps aux` ou `top` vê a senha em texto claro na lista de processos (`/proc/<pid>/cmdline`).

## Como funciona
Para automação segura sem expor a senha na linha de comando, combine **`--text --non-interactive --stdin`** enviando a senha através da entrada padrão (`stdin` via pipe ou descritor de arquivo), além de passar `--protect-hidden=no` e `--Slot` explícito.

## Exemplo
```bash
# Criar um container VeraCrypt de 100 MiB (AES + SHA-512 + ext4) em modo texto nao-interativo
veracrypt --text --create /cases/vaults/dfir_evidence.hc \
  --size=100M \
  --encryption=AES \
  --hash=sha512 \
  --filesystem=ext4 \
  --pim=0 \
  --keyfiles="" \
  --random-source=/dev/urandom \
  --non-interactive -p "Passphrase-Temporaria-Ou-Via-Stdin-2026!"
```

## Limites e trade-offs
Ao desmontar um contêiner em scripts de backup ou encerramento de sessão, use **`veracrypt --text --dismount /cases/vaults/dfir_evidence.hc`** (ou `--dismount` global) e verifique o código de saída; adicione `--force` apenas se um processo órfão estiver prendendo o ponto de montagem.

## Como verificar
Monte um contêiner em modo somente-leitura (`--mount-options=ro`) durante análises forenses para garantir preservação da evidência.

## Conexões
- [[veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho]] — Veja também: VeraCrypt: Arquitetura de Criptografia de Volumes Multiplataforma, Modo **XTS (IEEE P1619)**, **PBKDF2-RIPEMD160/SHA-512/Whirlpool/BLAKE2s** e **PIM**.
- [[veracrypt-cifras-cascata-aes-twofish-serpent-camellia-kuznyechik]] — Veja também: VeraCrypt: Cifras Individuais vs **Cifras em Cascata (*Cascades*: `AES-Twofish-Serpent`)** em Modo XTS e Impacto de Hardware `AES-NI`.
- [[veracrypt-autenticacao-multifator-keyfiles-pim-personal-iterations-multiplier]] — Referência cruzada direta com veracrypt-autenticacao-multifator-keyfiles-pim-personal-iterations-multiplier.
- [[cryptsetup-abertura-volumes-bitlocker-veracrypt-truecrypt-forense]] — Referência cruzada direta com cryptsetup-abertura-volumes-bitlocker-veracrypt-truecrypt-forense.

## Fontes
- [VeraCrypt Official GitHub Repository — Architecture & Reproducible Builds](https://raw.githubusercontent.com/veracrypt/VeraCrypt/master/README.md) — repositório oficial do VeraCrypt (IDRIX) cobrindo arquitetura criptográfica, builds reprodutíveis e verificação de assinaturas; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Command Line Usage Reference](https://veracrypt.io/en/Command%20Line%20Usage.html) — documentação oficial de linha de comando do VeraCrypt cobrindo criação, montagem, PIM, keyfiles e volumes ocultos; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Technical & Security Guide](https://veracrypt.io/en/Documentation.html) — guia técnico oficial do VeraCrypt sobre modo XTS, cifras em cascata, cabeçalho de backup e proteção de memória; consultado em 2026-10-03.
