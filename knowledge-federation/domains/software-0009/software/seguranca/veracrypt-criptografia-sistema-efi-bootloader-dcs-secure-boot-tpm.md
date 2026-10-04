---
id: software.seguranca.tranche08.000718
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

# VeraCrypt no Windows: Criptografia da Partição do Sistema Operacional (**VeraCrypt EFI Boot Loader `VeraCrypt-DCS`**) e Coexistência com **Secure Boot**

## Em uma frase
Em estações Windows, além de contêineres e discos de dados, o VeraCrypt permite criptografar a partição completa do sistema operacional Windows (*System Encryption* pré-boot) através do **VeraCrypt EFI Boot Loader** (projeto open-source `veracrypt/VeraCrypt-DCS`, licenciado sob LGPL).

## Por que importa
Quando a máquina liga, o firmware UEFI carrega `\EFI\VeraCrypt\DcsBoot.efi` antes do Windows Boot Manager: o `DcsBoot.efi` exibe o prompt de pré-boot, coleta a senha e o PIM, deriva a chave XTS na tela de boot e instala o filtro de disco em memória para que o kernel do Windows carregue de forma transparente.

## Como funciona
Conforme documentado no `README.md` oficial do VeraCrypt, os binários `.sys` e `.efi` oficiais são assinados digitalmente com o certificado da **IDRIX** (e cross-signed pela Microsoft para UEFI Secure Boot), permitindo manter o **UEFI Secure Boot** habilitado na BIOS.

## Exemplo
```powershell
# Verificar no Windows (PowerShell Admin) a assinatura Authenticode do driver de kernel veracrypt.sys da IDRIX
Get-AuthenticodeSignature "C:\Windows\System32\drivers\veracrypt.sys" | Format-List Status, SignerCertificate
```

## Limites e trade-offs
Ao usar criptografia de sistema VeraCrypt em notebooks Windows, gere e guarde obrigatoriamente o **VeraCrypt Rescue Disk** (um arquivo `.zip` contendo a partição EFI de recuperação específica daquela máquina, com o backup do cabeçalho daquele disco): sem o *Rescue Disk*, se uma grande atualização do Windows sobrescrever o bootloader EFI, o sistema não conseguirá iniciar.

## Como verificar
Verifique no utilitário `msinfo32` ou `Confirm-SecureBootUEFI` que o Secure Boot permanece ativo.

## Conexões
- [[veracrypt-higiene-memoria-ram-encryption-cold-boot-hibernacao-swap]] — Veja também: VeraCrypt: Criptografia de Chaves em Memória RAM, Mitigação de *Cold Boot / DMA Attacks*, Hibernação, Swap e `veracrypt -d`.
- [[veracrypt-interoperabilidade-nativa-linux-cryptsetup-tcrypt-open]] — Veja também: Interoperabilidade Forense e Operacional: Abertura Nativa de Volumes **VeraCrypt** no Kernel Linux via **`cryptsetup open --type tcrypt --veracrypt`**.
- [[veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho]] — Referência cruzada direta com veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho.
- [[veracrypt-backup-restauracao-cabecalho-volume-emergencia-corrupcao]] — Referência cruzada direta com veracrypt-backup-restauracao-cabecalho-volume-emergencia-corrupcao.
- [[hashcat-mapeamento-teclado-hex-salt-compressao-arquivos-fde]] — Referência cruzada direta com hashcat-mapeamento-teclado-hex-salt-compressao-arquivos-fde.

## Fontes
- [VeraCrypt Official GitHub Repository — Architecture & Reproducible Builds](https://raw.githubusercontent.com/veracrypt/VeraCrypt/master/README.md) — repositório oficial do VeraCrypt (IDRIX) cobrindo arquitetura criptográfica, builds reprodutíveis e verificação de assinaturas; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Command Line Usage Reference](https://veracrypt.io/en/Command%20Line%20Usage.html) — documentação oficial de linha de comando do VeraCrypt cobrindo criação, montagem, PIM, keyfiles e volumes ocultos; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Technical & Security Guide](https://veracrypt.io/en/Documentation.html) — guia técnico oficial do VeraCrypt sobre modo XTS, cifras em cascata, cabeçalho de backup e proteção de memória; consultado em 2026-10-03.
