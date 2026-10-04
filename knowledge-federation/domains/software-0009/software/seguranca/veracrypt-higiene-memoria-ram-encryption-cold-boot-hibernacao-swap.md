---
id: software.seguranca.tranche08.000717
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

# VeraCrypt: Criptografia de Chaves em Memória RAM, Mitigação de *Cold Boot / DMA Attacks*, Hibernação, Swap e `veracrypt -d`

## Em uma frase
Enquanto um volume criptografado (VeraCrypt, LUKS ou BitLocker) está montado e aberto, a **Chave Mestra XTS** precisa existir na memória RAM do kernel para cifrar e decifrar blocos em tempo real — o que historicamente torna sistemas ligados ou suspensos alvo de **extração forense de memória RAM** (via DMA/Thunderbolt, *Cold Boot Attack*, arquivo de hibernação `hiberfil.sys` ou dump de VM no hypervisor).

## Por que importa
No Windows, o VeraCrypt implementa **RAM Encryption para chaves e senhas** (usando ChaCha12 em páginas não-pagináveis para ofuscar as chaves mestras em repouso na RAM com chaves efêmeras em registradores), bloqueio de memória de paginação e limpeza automática das chaves em memória ao detectar desligamento, suspensão ou remoção de dispositivos.

## Como funciona
Em estações Linux e Windows que montam volumes confidenciais, é obrigatório **desativar a hibernação em disco não-criptografado** e garantir que a partição de **Swap** também esteja criptografada (ex.: `dm-crypt` com chave aleatória efêmera a cada boot em `/etc/crypttab`), além de desmontar todos os volumes (`veracrypt --text -d`) assim que a operação terminar.

## Exemplo
```bash
# Desmontar imediatamente todos os volumes VeraCrypt abertos e limpar chaves em cache na memoria do driver
veracrypt --text --dismount
```

## Limites e trade-offs
Mesmo com ofuscação de RAM, se uma máquina virtual estiver rodando sobre um hypervisor comprometido ou sob controle de um analista forense que tira um snapshot completo da RAM + registradores de CPU (`volatility3`), qualquer volume montado no momento do snapshot pode ter seus arquivos ou chaves extraídos; **o único estado criptograficamente seguro contra captura física de memória é o volume desmontado (`--dismount`)**.

## Como verificar
Audite no Linux com `swapon --show` que não existem partições ou arquivos de swap em texto claro quando manipular volumes VeraCrypt.

## Conexões
- [[veracrypt-backup-restauracao-cabecalho-volume-emergencia-corrupcao]] — Veja também: VeraCrypt: Estrutura de **Cabeçalho Primário vs Cabeçalho de Backup Embutido (`--restore-header`)** e Recuperação de Desastres.
- [[veracrypt-criptografia-sistema-efi-bootloader-dcs-secure-boot-tpm]] — Veja também: VeraCrypt no Windows: Criptografia da Partição do Sistema Operacional (**VeraCrypt EFI Boot Loader `VeraCrypt-DCS`**) e Coexistência com **Secure Boot**.
- [[veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho]] — Referência cruzada direta com veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho.
- [[volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins]] — Referência cruzada direta com volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins.
- [[cryptsetup-integracao-kernel-keyring-logon-keys-vk-caching]] — Referência cruzada direta com cryptsetup-integracao-kernel-keyring-logon-keys-vk-caching.

## Fontes
- [VeraCrypt Official GitHub Repository — Architecture & Reproducible Builds](https://raw.githubusercontent.com/veracrypt/VeraCrypt/master/README.md) — repositório oficial do VeraCrypt (IDRIX) cobrindo arquitetura criptográfica, builds reprodutíveis e verificação de assinaturas; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Command Line Usage Reference](https://veracrypt.io/en/Command%20Line%20Usage.html) — documentação oficial de linha de comando do VeraCrypt cobrindo criação, montagem, PIM, keyfiles e volumes ocultos; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Technical & Security Guide](https://veracrypt.io/en/Documentation.html) — guia técnico oficial do VeraCrypt sobre modo XTS, cifras em cascata, cabeçalho de backup e proteção de memória; consultado em 2026-10-03.
