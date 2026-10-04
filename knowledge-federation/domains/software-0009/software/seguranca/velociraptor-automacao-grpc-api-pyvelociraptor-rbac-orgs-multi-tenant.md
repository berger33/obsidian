---
id: software.seguranca.tranche03.000300
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

# Velociraptor Automação SOAR via `gRPC API` (`pyvelociraptor`), `Orgs` Multi-Tenant e Governança `RBAC` / `OIDC`

## Em uma frase
Conforme destacado na seção *Automation* de `docs.velociraptor.app/docs/overview/` (*"Velociraptor can be fully automated using a gRPC based API"*), toda ação disponível na GUI do Velociraptor é na verdade uma consulta VQL executada no servidor, podendo ser acionada remotamente por sistemas SOAR, pipelines de resposta a alertas do SIEM ou scripts Python (`pyvelociraptor`) através da **API gRPC autenticada por certificado mTLS (`api_client.yaml`)**!

## Por que importa
Quando o SIEM ou EDR emite um alerta de alta severidade em um host às 04:00 da manhã, esperar que um analista acorde para coletar a memória e a lista de conexões de rede daquele host perde dados voláteis críticos.

## Como funciona
Gerando uma credencial de API (`velociraptor --config server.config.yaml config api_client --name soar-bot --role investigator api_client.yaml`), seu playbook SOAR executa uma query VQL no servidor (`schedule_artifact(...)`) que dispara a coleta forense no endpoint no mesmo segundo em que o alerta do SIEM chega!

## Exemplo
```bash
# 1. Gerando um certificado de cliente de API gRPC com papel RBAC restrito (investigator ou reader):
velociraptor --config server.config.yaml config api_client \
  --name soar-automation-bot \
  --role investigator \
  soar_api_client.yaml

# 2. Executando uma consulta VQL remotamente no servidor Velociraptor usando a credencial de API mTLS:
velociraptor --api_config soar_api_client.yaml query "SELECT client_id, os_info.hostname FROM clients() LIMIT 10"
```

## Limites e trade-offs
Em ambientes de MSSP / Consultoria DFIR ou grandes corporações, utilize o recurso de **Multi-Tenancy (`Orgs`)** e **RBAC granular** (integrado a OIDC: Okta, Entra ID, Google, Keycloak) para isolar completamente os clientes e evidências de cada unidade de negócio ou cliente atendido.

## Como verificar
Teste o arquivo `soar_api_client.yaml` gerado executando `velociraptor --api_config soar_api_client.yaml query "SELECT * FROM info()"`.

## Conexões
- [[velociraptor-orquestracao-ferramentas-externas-thor-hayabusa-cybertriage-quarantine]] — Veja também: Velociraptor Orquestração de Ferramentas de Terceiros (`Tools`) e Resposta Ativa (`Windows.Remediation.Quarantine`).

## Fontes
- [Velociraptor Official Documentation — Overview (Incident Response Timeline, VQL Engine, Client-Server/Offline/Virtual Modes, Monitoring & gRPC API)](https://docs.velociraptor.app/docs/overview/) — Visão geral oficial da documentação do Velociraptor explicando a atuação no passado/presente/futuro do incidente, modos de operação, VQL e ecossistema; consultado em 2026-10-03.
- [Velociraptor GitHub — README.md (Endpoint Visibility and Collection Tool, Quick Start, Build Collector, Artifact Exchange & Platforms)](https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md) — README oficial do Velocidex/velociraptor documentando execução da GUI, criação de coletores locais e o repositório comunitário Artifact Exchange; consultado em 2026-10-03.
- [Velociraptor — Official GitHub Repository (Velocidex / Rapid7)](https://github.com/Velocidex/velociraptor) — Repositório oficial open-source do Velociraptor; consultado em 2026-10-03.
