---
id: software.seguranca.tranche08.000719
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

# Interoperabilidade Forense e Operacional: Abertura Nativa de Volumes **VeraCrypt** no Kernel Linux via **`cryptsetup open --type tcrypt --veracrypt`**

## Em uma frase
Em servidores Linux minimalistas, containers privilegiados ou imagens de resposta a incidentes DFIR onde apenas o pacote padrão `cryptsetup` da distribuição está instalado (sem o binário da IDRIX nem bibliotecas wxWidgets/FUSE), **o kernel Linux (`dm-crypt`) e o `cryptsetup` possuem suporte nativo embutido para abrir qualquer volume VeraCrypt!**

## Por que importa
Conforme documentado no `README.md` oficial do projeto `cryptsetup`, o tipo **`--type tcrypt`** combinado com a flag **`--veracrypt`** implementa toda a derivação PBKDF2, PIM (`--veracrypt-pim`), Keyfiles (`--key-file` pode ser repetido para múltiplos keyfiles!) e até abertura de volumes ocultos do VeraCrypt diretamente sobre o *Device Mapper* do kernel Linux (`libcryptsetup`).

## Como funciona
Isso elimina completamente a dependência de FUSE em servidores Linux e permite montar volumes VeraCrypt via `/etc/crypttab` ou `systemd-cryptsetup` com performance nativa de bloco do kernel.

## Exemplo
```bash
# Inspecionar metadados do cabecalho decifrado (tcryptDump) e abrir um container VeraCrypt nativamente via cryptsetup!
sudo cryptsetup tcryptDump --veracrypt --veracrypt-pim 0 /cases/vaults/dfir_evidence.hc
sudo cryptsetup open --type tcrypt --veracrypt --readonly /cases/vaults/dfir_evidence.hc vc_evidence
sudo mount -o ro /dev/mapper/vc_evidence /mnt/evidence
```

## Limites e trade-offs
Se o volume VeraCrypt tiver sido criado usando um número **PIM** customizado, passe **`--veracrypt-pim <numero>`** (ou `--veracrypt-query-pim` para que o `cryptsetup` pergunte o PIM no terminal) junto com `--type tcrypt --veracrypt`.

## Como verificar
Para fechar o volume aberto via `cryptsetup`, desmonte o filesystem (`sudo umount /mnt/evidence`) e execute **`sudo cryptsetup close vc_evidence`**.

## Conexões
- [[veracrypt-criptografia-sistema-efi-bootloader-dcs-secure-boot-tpm]] — Veja também: VeraCrypt no Windows: Criptografia da Partição do Sistema Operacional (**VeraCrypt EFI Boot Loader `VeraCrypt-DCS`**) e Coexistência com **Secure Boot**.
- [[veracrypt-builds-reprodutiveis-source-date-epoch-verificacao-pgp]] — Veja também: VeraCrypt: Verificação de Supply Chain — Assinaturas OpenPGP da IDRIX e **Builds Reprodutíveis (`SOURCE_DATE_EPOCH`)** para `.deb` e `.rpm`.
- [[veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho]] — Referência cruzada direta com veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho.
- [[cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup]] — Referência cruzada direta com cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup.
- [[cryptsetup-abertura-volumes-bitlocker-veracrypt-truecrypt-forense]] — Referência cruzada direta com cryptsetup-abertura-volumes-bitlocker-veracrypt-truecrypt-forense.

## Fontes
- [VeraCrypt Official GitHub Repository — Architecture & Reproducible Builds](https://raw.githubusercontent.com/veracrypt/VeraCrypt/master/README.md) — repositório oficial do VeraCrypt (IDRIX) cobrindo arquitetura criptográfica, builds reprodutíveis e verificação de assinaturas; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Command Line Usage Reference](https://veracrypt.io/en/Command%20Line%20Usage.html) — documentação oficial de linha de comando do VeraCrypt cobrindo criação, montagem, PIM, keyfiles e volumes ocultos; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Technical & Security Guide](https://veracrypt.io/en/Documentation.html) — guia técnico oficial do VeraCrypt sobre modo XTS, cifras em cascata, cabeçalho de backup e proteção de memória; consultado em 2026-10-03.
