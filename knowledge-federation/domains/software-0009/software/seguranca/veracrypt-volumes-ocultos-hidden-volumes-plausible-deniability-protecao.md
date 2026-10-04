---
id: software.seguranca.tranche08.000715
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

# VeraCrypt: **Hidden Volumes (*Plausible Deniability*)**, Funcionamento da Proteção de Volume Oculto (`--protect-hidden`) e Limites Forenses

## Em uma frase
O VeraCrypt implementa **Negação Plausível (*Plausible Deniability*)** através de **Volumes Ocultos (*Hidden Volumes*)**: dentro do espaço livre (que já é preenchido por bytes indistinguíveis de dados aleatórios) de um volume VeraCrypt externo (*Outer Volume*), cria-se um segundo volume independente cujo cabeçalho fica armazenado no offset `65536` (`64 KiB`) com uma **segunda senha diferente**.

## Por que importa
Qual dos dois volumes será montado depende exclusivamente de qual senha você digitar na montagem: se digitar a senha externa, o VeraCrypt decifra os primeiros 64 KiB e monta o volume externo (sem revelar que existe um volume oculto); se digitar a senha oculta, o VeraCrypt decifra os segundos 64 KiB e monta o volume oculto!

## Como funciona
Porém, existe um cuidado operacional vital: se você montar o **volume externo** em modo leitura/escrita e copiar arquivos grandes para ele sem ativar a **Proteção do Volume Oculto (`--protect-hidden=yes` + `--protection-password`)**, o sistema de arquivos do volume externo pode sobrescrever os blocos físicos onde mora o volume oculto!

## Exemplo
```bash
# Montar o volume externo ativando a protecao em memoria contra sobrescrita acidental dos blocos do volume oculto
veracrypt --text --mount /cases/vaults/dual_container.hc /mnt/outer \
  --protect-hidden=yes \
  --protection-password="Senha-Do-Volume-Oculto-Interno!" \
  --non-interactive --stdin <<< "Senha-Do-Volume-Externo!"
```

## Limites e trade-offs
Sob a ótica de **Forense Digital (DFIR)**, embora seja impossível provar matematicamente pela inspeção estática do arquivo `.hc` que existe um volume oculto dentro do espaço livre, artefatos deixados no **sistema operacional host** (como histórico `RecentFiles`, *Jump Lists* do Windows, *Shellbags*, logs do `systemd` ou arquivos `.DS_Store`/thumbnails apontando para caminhos que só existiam no volume oculto) revelam o uso se o volume não for aberto dentro de um SO amnésico/Live RAM.

## Como verificar
Ao montar qualquer volume oculto sensível, utilize sempre `--mount-options=ro,noatime` ou um ambiente Live em RAM sem swap em disco.

## Conexões
- [[veracrypt-autenticacao-multifator-keyfiles-pim-personal-iterations-multiplier]] — Veja também: VeraCrypt: Autenticação Multifator de Volumes com **Keyfiles**, Tokens PKCS#11 (YubiKey/SmartCard) e **PIM (*Personal Iterations Multiplier*)**.
- [[veracrypt-backup-restauracao-cabecalho-volume-emergencia-corrupcao]] — Veja também: VeraCrypt: Estrutura de **Cabeçalho Primário vs Cabeçalho de Backup Embutido (`--restore-header`)** e Recuperação de Desastres.
- [[veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho]] — Referência cruzada direta com veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho.
- [[veracrypt-higiene-memoria-ram-encryption-cold-boot-hibernacao-swap]] — Referência cruzada direta com veracrypt-higiene-memoria-ram-encryption-cold-boot-hibernacao-swap.
- [[volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins]] — Referência cruzada direta com volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins.

## Fontes
- [VeraCrypt Official GitHub Repository — Architecture & Reproducible Builds](https://raw.githubusercontent.com/veracrypt/VeraCrypt/master/README.md) — repositório oficial do VeraCrypt (IDRIX) cobrindo arquitetura criptográfica, builds reprodutíveis e verificação de assinaturas; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Command Line Usage Reference](https://veracrypt.io/en/Command%20Line%20Usage.html) — documentação oficial de linha de comando do VeraCrypt cobrindo criação, montagem, PIM, keyfiles e volumes ocultos; consultado em 2026-10-03.
- [VeraCrypt Official Documentation — Technical & Security Guide](https://veracrypt.io/en/Documentation.html) — guia técnico oficial do VeraCrypt sobre modo XTS, cifras em cascata, cabeçalho de backup e proteção de memória; consultado em 2026-10-03.
