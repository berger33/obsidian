---
id: software.seguranca.tranche03.000299
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

# Velociraptor Orquestração de Ferramentas de Terceiros (`Tools`) e Resposta Ativa (`Windows.Remediation.Quarantine`)

## Em uma frase
Conforme documentado na seção *Collection* de `docs.velociraptor.app/docs/overview/` (*"Velociraptor can also push third party tools to the endpoint, executing them remotely and transferring their results back to the server"*), o Velociraptor possui um gerenciador nativo de binários externos (**`Tools`**) que distribui sob demanda ferramentas forenses consagradas — como **Hayabusa**, **Nextron Thor**, **Cyber Triage**, **Sysinternals Autoruns**, **Capa** ou **WinPmem** — verifica seu hash SHA-256 no endpoint, executa-as e recolhe a saída estruturada!

## Por que importa
Implantar e atualizar manualmente binários de terceiros em milhares de máquinas antes de uma investigação é lento; o sistema de `Tools` do Velociraptor baixa o binário no endpoint apenas quando o artefato é acionado, armazena em cache local verificado por hash e parseia o JSON/CSV de saída dentro do próprio VQL!

## Como funciona
Para contenção ativa durante um ataque em andamento (por exemplo, propagação de ransomware), o artefato **`Windows.Remediation.Quarantine`** (e equivalente Linux via `iptables`/netfilter) isola a máquina da rede instantaneamente configurando políticas IPsec/Firewall que bloqueiam todo o tráfego exceto a conexão mTLS com o próprio servidor Velociraptor!

## Exemplo
```bash
# Listando as ferramentas externas registradas e seus hashes no servidor Velociraptor:
velociraptor --config server.config.yaml query "SELECT Name, Filename, Hash, ServeURL FROM server_tools()"
```

## Limites e trade-offs
Antes de executar `Windows.Remediation.Quarantine` em produção, teste o artefato de isolamento e o artefato de remoção de quarentena (`Quarantine` com `Action=Remove`) em uma VM de homologação para validar que o canal do Velociraptor permanece ativo.

## Como verificar
Verifique o catálogo de ferramentas na aba `Server Artifacts -> Tools` da GUI.

## Conexões
- [[velociraptor-notebooks-interativos-pos-processamento-vql-timesketch-siem]] — Veja também: Velociraptor `Notebooks` Colaborativos e Exportação (`Timesketch`, `Splunk`, `Elastic` e `S3`): análise pós-coleta sem reinterrogar o host.
- [[velociraptor-automacao-grpc-api-pyvelociraptor-rbac-orgs-multi-tenant]] — Veja também: Velociraptor Automação SOAR via `gRPC API` (`pyvelociraptor`), `Orgs` Multi-Tenant e Governança `RBAC` / `OIDC`.

## Fontes
- [Velociraptor Official Documentation — Overview (Incident Response Timeline, VQL Engine, Client-Server/Offline/Virtual Modes, Monitoring & gRPC API)](https://docs.velociraptor.app/docs/overview/) — Visão geral oficial da documentação do Velociraptor explicando a atuação no passado/presente/futuro do incidente, modos de operação, VQL e ecossistema; consultado em 2026-10-03.
- [Velociraptor GitHub — README.md (Endpoint Visibility and Collection Tool, Quick Start, Build Collector, Artifact Exchange & Platforms)](https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md) — README oficial do Velocidex/velociraptor documentando execução da GUI, criação de coletores locais e o repositório comunitário Artifact Exchange; consultado em 2026-10-03.
- [Velociraptor — Official GitHub Repository (Velocidex / Rapid7)](https://github.com/Velocidex/velociraptor) — Repositório oficial open-source do Velociraptor; consultado em 2026-10-03.
