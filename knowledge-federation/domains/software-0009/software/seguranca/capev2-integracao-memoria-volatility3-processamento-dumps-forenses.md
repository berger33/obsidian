---
id: software.seguranca.tranche06.000550
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
fontes: ["https://raw.githubusercontent.com/kevoreilly/CAPEv2/master/README.md", "https://capev2.readthedocs.io/en/latest/usage/api.html", "https://github.com/CAPESandbox/CAPE-parsers"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CAPEv2 Sandbox: Geração de Dumps Completos de Memória RAM (`memory=1`) e Pós-Processamento Integrado com **Volatility 3**

## Em uma frase
Quando uma tarefa é submetida ao CAPEv2 com o parâmetro **`memory=1`** (ou quando `memory_dump = on` está ativo em `cuckoo.conf`), o hipervisor KVM/QEMU salva um dump completo da memória RAM física da máquina virtual convidada no final da detonação, imediatamente antes de reverter o snapshot.

## Por que importa
Embora o `capemon` capture artefatos no espaço de usuário dos processos monitorados, ameaças que injetam código em processos de sistema excluídos do monitoramento ou que instalam drivers de kernel (*rootkits* / *BYOVD*) exigem análise forense completa da memória física da VM.

## Como funciona
O módulo de processamento de memória do CAPEv2 executa automaticamente plugins do **Volatility 3** (`pslist`, `pstree`, `malfind`, `netscan`, `callbacks`, `ssdt`, `ldrmodules`) sobre o dump `.dmp`/`.raw` da VM e anexa os resultados estruturados diretamente ao relatório final da tarefa.

## Exemplo
```bash
# Consultar na API do CAPEv2 os resultados do modulo de analise de memoria Volatility de uma tarefa
curl -sS -H "Authorization: Token ${CAPE_API_TOKEN}" \
  "http://127.0.0.1:8000/apiv2/tasks/report/1042/json/" | jq '.memory'
```

## Limites e trade-offs
Habilitar `memory=1` para 100% das submissões em uma fila de alto volume grava arquivos de 4 GB a 8 GB em disco por tarefa; habilite `memory=1` seletivamente para amostras críticas ou configure a limpeza automática de dumps antigos (`clean_memory`) após o processamento do Volatility 3.

## Como verificar
Submeta uma amostra com `memory=1` e verifique a população da chave `.memory` no relatório JSON após o término do processamento.

## Conexões
- [[capev2-roteamento-rede-inetsim-tor-vpn-isolamento-pcap]] — Veja também: CAPEv2 Sandbox: Roteamento Por Tarefa (`route=inetsim`, `route=tor`, `route=vpn`, `route=none`) e Prevenção de Abuso Lateral.
- [[capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara]] — Referência cruzada direta com capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara.
- [[volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins]] — Referência cruzada direta com volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins.
- [[volatility3-deteccao-injecao-memoria-malfind-hollowprocesses-vadinfo]] — Referência cruzada direta com volatility3-deteccao-injecao-memoria-malfind-hollowprocesses-vadinfo.

## Fontes
- [CAPEv2 Official GitHub — Malware Configuration And Payload Extraction](https://raw.githubusercontent.com/kevoreilly/CAPEv2/master/README.md) — documentação oficial do CAPEv2 cobrindo unpacking dinâmico, debugger programável por YARA, AMSI e CAPE-parsers; consultado em 2026-10-03.
- [CAPEv2 Official Documentation — REST API v2 Reference](https://capev2.readthedocs.io/en/latest/usage/api.html) — referência oficial da REST API v2 (/apiv2/), autenticação por token DRF, throttling e endpoints de tarefas; consultado em 2026-10-03.
- [CAPE-parsers Official Repository — Static Configuration Extractors](https://github.com/CAPESandbox/CAPE-parsers) — repositório oficial de extratores de configuração de famílias de malware do CAPEv2; consultado em 2026-10-03.
