---
id: software.seguranca.tranche12.001108
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/README.md", "https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/Cargo.toml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Autoria de **Regras Nativas do Chainsaw** e Mapeamentos Customizados no Formato **TAU Engine** (`filter`, `group`, `fields`)

## Em uma frase
Embora o formato **Sigma** seja o padrão universal para regras compartilhadas entre SIEMs, o formato de **Regra Nativa do Chainsaw** (baseado diretamente no **TAU Engine**) oferece recursos de apresentação e extração de campos específicos por artefato que permitem criar tabelas forenses sob medida para qualquer documento JSON/XML (inclusive artefatos que não são Event Logs)!

## Por que importa
Uma regra nativa do Chainsaw (`.yml`) define os metadados (`title`, `group`, `description`, `level`, `status`, `kind: evtx`), a seção **`filter`** (com expressões booleanas do TAU Engine, ex.: `condition: Event.System.EventID: =4720`) e a seção **`fields`** — que especifica exatamente quais campos do evento devem ser extraídos e exibidos como colunas nomeadas na saída da tabela ou CSV (ex.: `from: Event.EventData.TargetUserName`, `to: Usuario Criado`)!

## Como funciona
Isso explica por que a saída do Chainsaw para regras nativas de criação de usuários, brute-force ou RDP mostra colunas perfeitamente rotuladas (`User`, `Source IP`, `Logon Type`) em vez de um despejo genérico de campos!

## Exemplo
```yaml
# Exemplo de regra nativa do Chainsaw (formato TAU Engine) para extrair criacao de contas locais com colunas dedicadas
title: Criacao de Conta de Usuario Local
group: Persistencia - Contas
description: Detecta a criacao de uma nova conta de usuario (Event ID 4720)
kind: evtx
level: medium
status: stable
timestamp: Event.System.TimeCreated_attributes.SystemTime
fields:
  - name: Conta Criadora
    from: Event.EventData.SubjectUserName
  - name: Nova Conta Criada
    from: Event.EventData.TargetUserName
filter:
  condition: 'Event.System.EventID: =4720'
```

## Limites e trade-offs
Você pode criar regras nativas do Chainsaw não apenas para `.evtx`, mas também para documentos JSON gerados por outros parsers forenses, bastando ajustar os caminhos de `timestamp`, `fields` e `filter`!

## Como verificar
Armazene suas regras nativas customizadas em um diretório versionado no Git e passe-o via `-r ./minhas-regras-chainsaw/` durante o `chainsaw hunt`.

## Conexões
- [[chainsaw-regras-nativas-av-alerts-defender-sophos-kaspersky-evtx]] — Veja também: Triagem de Alertas de Antivírus/EDR (**Windows Defender, Sophos, F-Secure e Kaspersky**) e Limpeza de Logs com as Regras Nativas do Chainsaw.
- [[chainsaw-deteccao-movimentacao-lateral-logins-brute-force-contas]] — Veja também: Investigação de **Movimentação Lateral, Brute-Force e Escalação de Privilégio** (`lateral_movement` e `security`) com o Chainsaw.
- [[chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust]] — Referência cruzada direta com chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust.
- [[chainsaw-hunting-regras-sigma-tau-engine-mappings-evtx]] — Referência cruzada direta com chainsaw-hunting-regras-sigma-tau-engine-mappings-evtx.
- [[sigma-logica-detection-modificadores-valores-base64offset-windash-re]] — Referência cruzada direta com sigma-logica-detection-modificadores-valores-base64offset-windash-re.

## Fontes
- [WithSecure Chainsaw Official GitHub — Rapidly Search and Hunt Through Windows Forensic Artefacts](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/README.md) — repositório oficial do Chainsaw cobrindo triagem forense (`hunt`, `search`, `analyse shimcache`, `analyse srum`, `dump`), regras Sigma e motor TAU; consultado em 2026-10-03.
- [WithSecure Chainsaw Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/Cargo.toml) — especificação oficial das bibliotecas forenses em Rust do Chainsaw 2.16+ (`evtx`, `mft`, `notatin`, `libesedb`, `tau-engine`, `aho-corasick`, `rayon`); consultado em 2026-10-03.
