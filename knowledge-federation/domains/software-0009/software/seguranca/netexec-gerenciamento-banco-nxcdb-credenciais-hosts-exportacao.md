---
id: software.seguranca.tranche06.000599
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/Pennyw0rth/NetExec/main/README.md", "https://www.netexec.wiki/getting-started/installation", "https://github.com/Pennyw0rth/NetExec"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# NetExec (`nxcdb`): Consulta Estruturada do Banco de Dados de Auditoria (`hosts`, `creds`, `admin`, `shares`) e Reutilização por ID (`-id`)

## Em uma frase
O utilitário interativo **`nxcdb`** gerencia os bancos SQLite alimentados automaticamente por cada execução do `nxc`, permitindo consultar hosts, credenciais, compartilhamentos e relações de administração e exportar evidências em CSV.

## Por que importa
Depois que uma credencial (senha ou hash) é validada uma vez pelo `nxc`, ela recebe um **`CredID`** numérico no `nxcdb`: nas execuções seguintes do `nxc`, o auditor pode passar simplesmente **`-id <CredID>`** (ex.: `nxc smb 10.10.20.55 -id 3 --shares`) sem nunca mais precisar digitar ou expor a senha ou o hash NTLM na linha de comando ou no histórico do shell (`~/.bash_history` / `~/.zsh_history`).

## Como funciona
Dentro do `nxcdb`, trocar de protocolo (`proto smb`, `proto ldap`, `proto mssql`, `proto ssh`) disponibiliza comandos dedicados como `hosts`, `creds`, `shares`, `disks`, `users`, `groups` e `export creds /cases/pentest/creds_audit.csv`.

## Exemplo
```bash
# Consultar credenciais armazenadas no nxcdb e reutilizar a credencial pelo seu ID numerico (-id 1) sem expor a senha no shell
nxcdb -e "proto smb; creds; hosts"
nxc smb 10.10.20.55 -id 1 --shares
```

## Limites e trade-offs
Usar **`-id <CredID>`** é uma prática essencial de higiene operacional: evita que senhas descobertas fiquem visíveis em `ps aux` ou gravadas em arquivos de histórico de terminal da máquina de auditoria.

## Como verificar
Ao concluir uma auditoria autorizada, exporte as evidências do workspace e arquive/remova de forma segura o diretório `~/.nxc/workspaces/<cliente>/`.

## Conexões
- [[netexec-modulos-auditoria-adcs-petitpotam-nopac-zerologon-slinky]] — Veja também: NetExec: Catálogo de Módulos (`-M` / `--list-modules`) para Auditoria de **AD CS**, **Coerção RPC** (`coerce_plus`), **WebDAV** e **LAPS**.
- [[netexec-deteccao-blue-team-telemetria-windows-zeek-suricata-hardening]] — Veja também: Detecção do NetExec pelo **Blue Team** (Correlação de Eventos Windows `4624`/`4625`/`5140`/`5145`/`4697`, Zeek e Hardening de Tiering AD).
- [[netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces]] — Referência cruzada direta com netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces.
- [[netexec-protocolo-smb-enumeracao-signing-shares-sessoes-disks]] — Referência cruzada direta com netexec-protocolo-smb-enumeracao-signing-shares-sessoes-disks.

## Fontes
- [NetExec Official GitHub — The Network Execution Tool (nxc & nxcdb)](https://raw.githubusercontent.com/Pennyw0rth/NetExec/main/README.md) — documentação oficial do NetExec cobrindo protocolos suportados, instalação via pipx e banco nxcdb; consultado em 2026-10-03.
- [NetExec Official Wiki — Getting Started & Protocol Usage](https://www.netexec.wiki/getting-started/installation) — wiki oficial do NetExec cobrindo instalação, autenticação Kerberos/NTLM, módulos e operação; consultado em 2026-10-03.
- [NetExec Official Repository](https://github.com/Pennyw0rth/NetExec) — repositório oficial do projeto NetExec; consultado em 2026-10-03.
