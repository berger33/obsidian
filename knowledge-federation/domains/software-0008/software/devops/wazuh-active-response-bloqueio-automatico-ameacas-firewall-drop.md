---
id: software.devops.tranche20.001966
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/wazuh/wazuh/master/README.md", "https://documentation.wazuh.com/current/getting-started/components/index.html", "https://github.com/wazuh/wazuh"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Wazuh Active Response: execução automatizada de contramedidas (`firewall-drop`, bloqueio de IP e isolamento) sob ataque

## Em uma frase
O recurso **Active Response** do Wazuh executa scripts de contramedida automatizados no agente afetado (ou em outros agentes/gateways) assim que uma regra específica ou um limiar de severidade (ex.: `level >= 10` de força bruta ou exploit web) é disparado no Wazuh Server.

## Por que importa
Detectar um ataque de força bruta SSH ou varredura de vulnerabilidade em tempo real e apenas gravar um alerta para ser lido horas depois permite que o invasor continue tentando milhares de combinações.

## Como funciona
No `ossec.conf` do servidor, um bloco `<command>` referencia um script homologado (como `firewall-drop`, `host-deny`, `route-null` ou script customizado) com `<timeout_allowed>yes</timeout_allowed>`, e um bloco `<active-response>` vincula o comando às regras (`<rules_id>5763</rules_id>`) com um `<timeout>600</timeout>`: o agente bloqueia o IP atacante no `iptables`/`nftables` local imediatamente e remove o bloqueio automaticamente após 600 segundos.

## Exemplo
```xml
<active-response>
  <command>firewall-drop</command>
  <location>local</location>
  <rules_id>5763,31151</rules_id>
  <timeout>600</timeout>
</active-response>
```

## Limites e trade-offs
Declare sempre seus IPs de gerência, gateways internos, servidores DNS e proxies confiáveis na lista `<white_list>` da seção `<global>` do `ossec.conf` para impedir que um atacante com IP falsificado provoque um *Self-DoS* via Active Response.

## Como verificar
Monitore todas as ações de bloqueio e desbloqueio executadas pelo Active Response no arquivo `/var/ossec/logs/active-responses.log` do endpoint.

## Conexões
- [[wazuh-log-analysis-decoders-rules-xml-teste-wazuh-logtest]] — Veja também: Wazuh Análise de Logs: criação de `decoders` e `rules` customizados e validação interativa com `wazuh-logtest`.
- [[wazuh-seguranca-containers-docker-listener-kubernetes-audit-logs]] — Veja também: Wazuh para Containers e Kubernetes: integração nativa com Docker Engine (`docker-listener`) e Kubernetes Audit Webhook.

## Fontes
- [Wazuh GitHub — README.md (Open Source XDR and SIEM Platform for Endpoints and Cloud Workloads)](https://raw.githubusercontent.com/wazuh/wazuh/master/README.md) — README oficial do wazuh/wazuh resumindo capacidades de XDR/SIEM, FIM, SCA, detecção de vulnerabilidades, Active Response e monitoramento de containers e nuvem; consultado em 2026-10-03.
- [Wazuh Official Documentation — Components (Wazuh Agent, Wazuh Server, Wazuh Indexer, Wazuh Dashboard & Agentless Monitoring)](https://documentation.wazuh.com/current/getting-started/components/index.html) — Documentação oficial de arquitetura dos componentes centrais do Wazuh e comunicação criptografada entre agentes, servidor e indexador; consultado em 2026-10-03.
- [Wazuh — Official GitHub Repository](https://github.com/wazuh/wazuh) — Repositório oficial GPLv2 do Wazuh; consultado em 2026-10-03.
