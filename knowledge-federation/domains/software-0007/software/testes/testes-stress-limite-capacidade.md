---
id: software.testes.tranche07.000105
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://grafana.com/docs/k6/latest/testing-guides/test-types/stress-testing/", "https://sre.google/sre-book/testing-reliability/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Stress test para revelar limites de capacidade", "Teste: Stress test para revelar limites de capacidade"]
lote: software-testes-2000-0001
---

# Stress test para revelar limites de capacidade

## Em uma frase
Aumente a carga de forma controlada acima do padrão esperado para observar degradação, ponto de saturação e recuperação.

## Por que importa
Conhecer o comportamento perto do limite ajuda a prever falhas, proteger dependências e decidir se é necessário escalar, rejeitar tráfego ou reduzir funcionalidade.

## Como funciona
Escolha um objetivo explícito — capacidade de pico, margem operacional ou comportamento em sobrecarga — e progrida carga em etapas. Observe filas, erros, latência, CPU, memória e dependências; interrompa se o ensaio ultrapassar o blast radius acordado.

## Exemplo
Em ambiente isolado, eleve gradualmente as requisições de busca até que um threshold falhe; registre em que etapa ocorre saturação e se o serviço mantém operações essenciais ou começa a falhar em cascata.

## Limites e trade-offs
Stress test não deve ser executado contra produção compartilhada sem autorização e controles. O ponto medido depende de hardware, tráfego, dados, dependências e configuração do gerador.

## Como verificar
Defina limites de parada, alarme e responsável antes do ensaio; verifique que a carga observada corresponde à gerada e registre os sintomas antes, durante e depois da saturação.

## Conexões
- [[chaos-experiments-steady-state-blast-radius]] — aprofundamento relacionado.
- [[performance-testing-modelagem-carga]] — aprofundamento relacionado.

## Fontes
- [Grafana k6 — Stress testing](https://grafana.com/docs/k6/latest/testing-guides/test-types/stress-testing/) — comportamento sob carga de pico ou acima da carga habitual; consultado em 2026-10-01.
- [Google SRE — Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — testes reduzem incerteza sobre confiabilidade após mudanças; consultado em 2026-10-01.
