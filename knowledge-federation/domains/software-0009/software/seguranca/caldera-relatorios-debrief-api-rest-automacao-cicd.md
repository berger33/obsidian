---
id: software.seguranca.tranche12.001127
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
fontes: ["https://raw.githubusercontent.com/mitre/caldera/master/README.md", "https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Automação via **API REST v2 (`/api/v2/operations`)** e Relatórios Executivos/Técnicos com o Plugin **`debrief`** do Caldera

## Em uma frase
Para transformar a validação de controles de segurança em um processo contínuo (**Continuous Security Validation / BAS — *Breach and Attack Simulation***), você pode controlar 100% do MITRE Caldera via sua **API RESTful v2** (documentada via Swagger/OpenAPI em `/api/docs`) e gerar relatórios PDF e grafos de ataque com o plugin **`debrief`**!

## Por que importa
Através do endpoint **`POST /api/v2/operations`**, um pipeline de CI/CD ou agendador de segurança inicia uma operação passando o ID do `adversary`, o `group` de agentes de homologação, o `planner` e o `obfuscator`, aguarda o estado mudar para `finished` e exporta o **`event-logs`** completo da operação (compatível com ATTIRE/JSON) para comparação automática com os alertas gerados no SIEM!

## Como funciona
Em seguida, o plugin **`debrief`** (`mitre/debrief`) renderiza grafos visuais da campanha (mostrando a progressão exata C2 -> Agente -> Tática -> Técnica -> Fatos Descobertos) e exporta um **Relatório PDF Executivo e Técnico** completo da operação!

## Exemplo
```bash
# Iniciar uma operacao automatizada no Caldera via API REST v2 e consultar o relatorio de event-logs ao final
CALDERA_API_KEY="ADMIN123"
OP_ID=$(curl -sS -X POST http://127.0.0.1:8888/api/v2/operations \
  -H "KEY: ${CALDERA_API_KEY}" -H "Content-Type: application/json" \
  -d '{"name":"PurpleTeam-Nightly-Run","adversary":{"adversary_id":"de526729-145f-459b-9824-4b28a2f7673b"},"group":"homolog-linux","autonomous":1}' | jq -r '.id')

curl -sS -X POST "http://127.0.0.1:8888/api/v2/operations/${OP_ID}/report" \
  -H "KEY: ${CALDERA_API_KEY}" -H "Content-Type: application/json" \
  -d '{"enable_agent_output":true}' | jq '{name: .name, start: .start, total_steps: (.steps | length)}'
```

## Limites e trade-offs
Com `enable_agent_output: true` na requisição ao endpoint `/api/v2/operations/{id}/report`, o JSON retornado inclui o comando decodificado, o `pid` do processo no sistema operacional alvo, o status de saída e o `stdout`/`stderr` de cada passo.

## Como verificar
Integre a saída do `/report` do Caldera com a API do seu SIEM para falhar o job de validação noturna caso alguma técnica crítica do perfil adversário não gere o alerta correspondente.

## Conexões
- [[caldera-operacoes-blue-team-response-gameboard-purple-team]] — Veja também: Caldera para o **Blue Team e Purple Team**: Plugins **`response`**, **`gameboard`** e **`compass`** para Defesa Automatizada e Visualização Conjunta.
- [[caldera-movimentacao-lateral-descoberta-fatos-credenciais-smb-ssh]] — Veja também: Emulação Automática de **Movimentação Lateral** no Caldera: Encadeando Descoberta de Sub-rede, Extração de Credenciais e Pivô SMB/SSH/WinRM.
- [[caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins]] — Referência cruzada direta com caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins.
- [[atomicredteam-logging-estruturado-executionlog-correlacao-siem-edr]] — Referência cruzada direta com atomicredteam-logging-estruturado-executionlog-correlacao-siem-edr.

## Fontes
- [MITRE Caldera Official GitHub — Automated Adversary Emulation, Red Team & Incident Response Platform](https://raw.githubusercontent.com/mitre/caldera/master/README.md) — repositório oficial do MITRE Caldera v5 cobrindo o Core C2 Server, interface VueJS Magma e ecossistema de plugins (`sandcat`, `stockpile`, `atomic`, `emu`, `debrief`, `response`); consultado em 2026-10-03.
- [MITRE Caldera Official Documentation — Learning the Terminology (`Agents`, `Abilities`, `Adversaries`, `Operations`, `Planners`, `Facts`, `Parsers`)](https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html) — documentação oficial ReadTheDocs detalhando a arquitetura de planejamento orientado a fatos e agentes do Caldera; consultado em 2026-10-03.
