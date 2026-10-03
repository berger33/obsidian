---
id: software.testes.tranche16.000977
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://github.com/tsenart/vegeta", "https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Vegeta: distinguir taxa, trabalhadores e conexões

## Em uma frase
A taxa define quantas requisições iniciar por segundo, os trabalhadores definem o paralelismo inicial e as conexões limitam conexões ociosas por host.

## Por que importa
Ajustar esses parâmetros sem entender seus papéis produz execuções que medem o cliente de carga em vez do serviço avaliado.

## Como funciona
Mantenha taxa e trabalhadores coerentes com o alvo, aumente conexões quando o protocolo permitir reaproveitamento e monitore os recursos da máquina geradora.

## Exemplo
Uma taxa alta com poucos trabalhadores faz a fila crescer no gerador, enquanto conexões insuficientes forçam abertura e fechamento constantes de sockets.

## Limites e trade-offs
Valores padrão servem para começar, mas não são adequados a todos os alvos; o comportamento observado, e não a intuição, orienta o ajuste.

## Como verificar
Execute a mesma carga com dois valores de trabalhadores e compare a taxa efetivamente alcançada para identificar o gargalo no gerador.

## Conexões
- [[vegeta-encode-and-dump]] — Veja também: Vegeta: converter resultados em formatos analisáveis.
- [[vegeta-timeouts-and-transport]] — Veja também: Vegeta: configurar tempo limite e transporte HTTP.

## Fontes
- [Vegeta — repositório oficial](https://github.com/tsenart/vegeta) — manual de uso: attack, report, plot, encode, dump e opções de conexão; consultado em 2026-10-03.
- [Vegeta — biblioteca Go](https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib) — API de taxa, atacante, alvos e métricas para uso programático; consultado em 2026-10-03.
