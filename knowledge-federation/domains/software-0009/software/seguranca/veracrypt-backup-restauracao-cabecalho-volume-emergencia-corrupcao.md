---
id: software.seguranca.tranche08.000716
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

# VeraCrypt: Estrutura de **Cabeçalho Primário vs Cabeçalho de Backup Embutido (`--restore-header`)** e Recuperação de Desastres

## Em uma frase
Nos primeiros 512 bytes do cabeçalho de 64 KiB de qualquer volume VeraCrypt residem o *salt* de 64 bytes e a **Chave Mestra XTS (Master Key)** criptografada com a chave derivada da sua senha; os setores de dados do volume são cifrados com a **Master Key** (e não diretamente com a sua senha).

## Por que importa
Isso traz duas consequências críticas para a engenharia de segurança e disponibilidade: **(1)** quando você troca a senha de um volume VeraCrypt de 4 TB (`--change`), o VeraCrypt **não** precisa re-criptografar os 4 TB de dados (ele apenas re-criptografa o cabeçalho de 64 KiB com a nova senha em segundos!); e **(2)** se os primeiros 64 KiB do disco sofrerem corrupção física (bad blocks ou sobrescrita acidental de tabela de partição), **100% dos 4 TB seriam perdidos para sempre se não houvesse backup do cabeçalho**!

## Como funciona
Todo volume criado pelo VeraCrypt possui um **Cabeçalho de Backup embutido nos últimos 64 KiB do volume**, que pode ser usado diretamente na montagem com **`--mount-options=headerbak`** ou restaurado com `--restore-header`, além de permitir exportar um arquivo de backup externo.

## Exemplo
```bash
# Montar um volume VeraCrypt cujo cabecalho primario no inicio do arquivo foi corrompido usando o cabecalho de backup embutido
veracrypt --text --mount /cases/vaults/damaged_primary.hc /mnt/recovery \
  --mount-options=headerbak,ro \
  --non-interactive --stdin <<< "Passphrase-Forte-2026!"
```

## Limites e trade-offs
Cuidado: como o cabeçalho de backup externo contém a mesma *Master Key* cifrada com a senha que estava ativa quando o backup foi feito, se um funcionário sair da empresa e você apenas trocar a senha do volume (`--change`), um atacante que possua o arquivo de backup antigo do cabeçalho **e** a senha antiga ainda conseguirá decifrar o volume inteiro! Para revogar a própria *Master Key*, é obrigatório criar um novo volume do zero.

## Como verificar
Sempre teste a montagem com `--mount-options=headerbak,ro` em procedimentos de validação de recuperação de desastres.

## Conexões
- [[veracrypt-volumes-ocultos-hidden-volumes-plausible-deniability-protecao]] — Veja também: VeraCrypt: **Hidden Volumes (*Plausible Deniability*)**, Funcionamento da Proteção de Volume Oculto (`--protect-hidden`) e Limites Forenses.
- [[veracrypt-higiene-memoria-ram-encryption-cold-boot-hibernacao-swap]] — Veja também: VeraCrypt: Criptografia de Chaves em Memória RAM, Mitigação de *Cold Boot / DMA Attacks*, Hibernação, Swap e `veracrypt -d`.
- [[veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho]] — Referência cruzada direta com veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho.
- [[cryptsetup-backup-restauracao-cabecalho-luksheaderbackup-luksheaderrestore]] — Referência cruzada direta com cryptsetup-backup-restauracao-cabecalho-luksheaderbackup-luksheaderrestore.
- [[cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey]] — Referência cruzada direta com cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey.

## Fontes
- [VeraCrypt Official GitHub Repository — Architecture & Reproducible Builds](https://raw.githubusercontent.com/veracrypt/VeraCrypt/master/README.md) — repositório oficial do VeraCrypt (IDRIX) cobrindo arquitetura criptográfica, builds reprodutíveis e verificação de assinaturas; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Command Line Usage Reference](https://veracrypt.io/en/Command%20Line%20Usage.html) — documentação oficial de linha de comando do VeraCrypt cobrindo criação, montagem, PIM, keyfiles e volumes ocultos; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Technical & Security Guide](https://veracrypt.io/en/Documentation.html) — guia técnico oficial do VeraCrypt sobre modo XTS, cifras em cascata, cabeçalho de backup e proteção de memória; consultado em 2026-10-03.
