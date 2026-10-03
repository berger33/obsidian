---
id: software.seguranca.tranche03.000292
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://docs.velociraptor.app/docs/overview/", "https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md", "https://github.com/Velocidex/velociraptor"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Velociraptor Query Language (`VQL`): consultas reativas com plugins geradores de linhas (`pslist`, `glob`, `parse_mft`, `yara`) e `foreach()`

## Em uma frase
Conforme destacado na seção *VQL - the Velociraptor difference* (`docs.velociraptor.app/docs/overview/`), diferente do osquery (que usa SQLite completo com tabelas fixas em C++), o **VQL (*Velociraptor Query Language*)** é uma linguagem de fluxo de dados em streaming onde **plugins geradores de linhas** ocupam a cláusula `FROM` e são encadeados de forma assíncrona através do plugin iterador **`foreach(row=..., query=...)`**!

## Por que importa
Em uma investigação DFIR real, você não quer apenas listar arquivos: você quer buscar arquivos modificados nas últimas 24h (`glob()`), ler o cabeçalho PE de cada um (`parse_pe()`), calcular o hash SHA-256 (`hash()`) e rodar regras YARA (`yara()`) em um único pipeline sem transferir gigabytes para o servidor.

## Como funciona
No VQL, você define variáveis intermediárias com **`LET`**, armazena funções reutilizáveis e encadeia plugins com `foreach()`, processando tudo diretamente na memória do endpoint e enviando ao servidor apenas as linhas que casaram com a investigação!

## Exemplo
```sql
-- Exemplo de query VQL listando processos cujo binário não está assinado ou executa a partir de pastas temporárias:
LET TempProcs = SELECT Pid, Name, Exe, CommandLine, Username
  FROM pslist()
  WHERE Exe =~ "(?i)(temp|tmp|appdata)"

SELECT Pid, Name, Exe, CommandLine, hash(path=Exe) AS Hashes
FROM TempProcs
```

## Limites e trade-offs
Você pode testar qualquer query VQL instantaneamente na linha de comando local (sem servidor) executando **`velociraptor query "SELECT * FROM info()"`**!

## Como verificar
Execute `velociraptor query "SELECT Pid, Name, Exe FROM pslist() LIMIT 10" --format jsonl` no terminal para validar o motor VQL.

## Conexões
- [[velociraptor-arquitetura-dfir-endpoint-visibility-vql-client-server]] — Veja também: Rapid7 Velociraptor: arquitetura da plataforma open-source de `DFIR` e visibilidade de endpoints movida por `VQL`.
- [[velociraptor-artifacts-yaml-client-server-events-artifact-exchange]] — Veja também: Velociraptor `Artifacts` e `Artifact Exchange`: empacotamento YAML de queries VQL (`CLIENT`, `SERVER`, `CLIENT_EVENT`, `SERVER_EVENT`).

## Fontes
- [Velociraptor Official Documentation — Overview (Incident Response Timeline, VQL Engine, Client-Server/Offline/Virtual Modes, Monitoring & gRPC API)](https://docs.velociraptor.app/docs/overview/) — Visão geral oficial da documentação do Velociraptor explicando a atuação no passado/presente/futuro do incidente, modos de operação, VQL e ecossistema; consultado em 2026-10-03.
- [Velociraptor GitHub — README.md (Endpoint Visibility and Collection Tool, Quick Start, Build Collector, Artifact Exchange & Platforms)](https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md) — README oficial do Velocidex/velociraptor documentando execução da GUI, criação de coletores locais e o repositório comunitário Artifact Exchange; consultado em 2026-10-03.
- [Velociraptor — Official GitHub Repository (Velocidex / Rapid7)](https://github.com/Velocidex/velociraptor) — Repositório oficial open-source do Velociraptor; consultado em 2026-10-03.
