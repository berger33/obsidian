---
id: software.testes.tranche11.000519
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://docs.locust.io/en/stable/increasing-request-rate.html", "https://docs.locust.io/en/stable/running-distributed.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: separar limite do gerador do limite do serviço

## Em uma frase
FastHttpUser pode reduzir overhead de cliente HTTP quando Locust precisa gerar uma taxa alta de requests.

## Por que importa
CPU saturada no gerador pode parecer throughput máximo do serviço, levando a uma conclusão errada sobre capacidade do sistema testado.

## Como funciona
Monitore recursos do load generator e compare cliente HTTP padrão/rápido sob a mesma hipótese, payload e perfil.

## Exemplo
Aumentar workers eleva taxa até um limite; experimento separado compara taxa possível sem confundir esse ganho com mudança do servidor.

## Limites e trade-offs
FastHttpUser altera custo do cliente e não reproduz browser; comparações requerem controles de rede e payload.

## Como verificar
Verifique CPU do gerador, warnings e latência do servidor para distinguir saturação do cliente de gargalo do alvo.

## Conexões
- [[locust-distributed-master-worker]] — Veja também: Locust: dimensionar master e workers sem atribuir carga ao master.

## Fontes
- [Locust 2.46 — Increasing the request rate](https://docs.locust.io/en/stable/increasing-request-rate.html) — diagnóstico de throughput, concorrência, saturação do gerador e uso de FastHttpUser para reduzir CPU; consultado em 2026-10-02.
- [Locust — Distributed load generation](https://docs.locust.io/en/stable/running-distributed.html) — processos master/worker, distribuição de carga, mensagens e limitações; consultado em 2026-10-02.
