---
id: software.devops.tranche20.001965
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

# Wazuh Análise de Logs: criação de `decoders` e `rules` customizados e validação interativa com `wazuh-logtest`

## Em uma frase
No Wazuh Server, o motor de análise de logs processa eventos recebidos dos agentes ou via Syslog em duas fases: primeiro os **Decoders** extraem campos estruturados (IP de origem, usuário, URL, status) da linha de log bruta, e em seguida as **Rules** (classificadas por níveis de severidade de `0` a `15`) avaliam condições, frequências e correlações temporais.

## Por que importa
Antes de implantar uma nova regra de detecção em produção, o engenheiro de segurança precisa testar se uma linha de log real da aplicação aciona o decoder esperado e qual nível de alerta é gerado, sem reiniciar o cluster do Wazuh Manager.

## Como funciona
O utilitário de linha de comando **`/var/ossec/bin/wazuh-logtest`** abre uma sessão interativa (ou recebe linhas via `stdin`) que simula exatamente o pipeline do `wazuh-analysisd`, exibindo em detalhes a Fase 1 (*pre-decoding*), a Fase 2 (*decoding* e campos extraídos) e a Fase 3 (*rule matching*, `id`, `level` e grupos).

## Exemplo
```bash
# Testando uma linha de log SSH contra os decoders e regras do Wazuh Server sem reiniciar o serviço:
echo 'Oct 03 14:22:01 web01 sshd[1942]: Failed password for invalid user admin from 203.0.113.55 port 49122 ssh2' \
  | /var/ossec/bin/wazuh-logtest
```

## Limites e trade-offs
Adicione sempre seus decoders e regras customizados nos arquivos **`/var/ossec/etc/decoders/local_decoder.xml`** e **`/var/ossec/etc/rules/local_rules.xml`** (usando IDs de regra na faixa `100000`–`120000`), pois os arquivos padrão em `/var/ossec/ruleset/` são sobrescritos durante upgrades do Wazuh.

## Como verificar
Execute `/var/ossec/bin/wazuh-analysisd -t` para validar a sintaxe XML de todos os decoders e regras antes de reiniciar o `wazuh-manager`.

## Conexões
- [[wazuh-security-configuration-assessment-sca-cis-benchmarks-hardening]] — Veja também: Wazuh Security Configuration Assessment (`SCA`): auditoria contínua de hardening e CIS Benchmarks como código.
- [[wazuh-active-response-bloqueio-automatico-ameacas-firewall-drop]] — Veja também: Wazuh Active Response: execução automatizada de contramedidas (`firewall-drop`, bloqueio de IP e isolamento) sob ataque.

## Fontes
- [Wazuh GitHub — README.md (Open Source XDR and SIEM Platform for Endpoints and Cloud Workloads)](https://raw.githubusercontent.com/wazuh/wazuh/master/README.md) — README oficial do wazuh/wazuh resumindo capacidades de XDR/SIEM, FIM, SCA, detecção de vulnerabilidades, Active Response e monitoramento de containers e nuvem; consultado em 2026-10-03.
- [Wazuh Official Documentation — Components (Wazuh Agent, Wazuh Server, Wazuh Indexer, Wazuh Dashboard & Agentless Monitoring)](https://documentation.wazuh.com/current/getting-started/components/index.html) — Documentação oficial de arquitetura dos componentes centrais do Wazuh e comunicação criptografada entre agentes, servidor e indexador; consultado em 2026-10-03.
- [Wazuh — Official GitHub Repository](https://github.com/wazuh/wazuh) — Repositório oficial GPLv2 do Wazuh; consultado em 2026-10-03.
