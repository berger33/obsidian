---
id: software.testes.tranche15.000900
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://kotest.io/docs/framework/isolation-mode.html", "https://kotest.io/docs/framework/project-config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest 6.2: preferir InstancePerRoot para isolamento de estado por raiz

## Em uma frase
O isolation mode decide quantas instâncias de uma Spec o engine cria; `InstancePerRoot` cria uma nova instância para cada teste de nível superior e compartilha essa instância com seus descendentes.

## Por que importa
Esse comportamento permite reiniciar campos de instância entre cenários principais sem recriar a estrutura declarada para cada nó interno.

## Como funciona
Na documentação atual, `InstancePerTest` e `InstancePerLeaf` aparecem como depreciados por comportamentos indefinidos em casos de borda.

## Exemplo
Se dois testes raiz não devem compartilhar um contador mutável, configure `isolationMode = IsolationMode.InstancePerRoot` e mantenha os casos subordinados sob a raiz cujo estado devem compartilhar.

## Limites e trade-offs
Modo de isolamento não reseta automaticamente singleton, banco ou variáveis globais; mudar o número de instâncias também altera quando hooks de spec são invocados.

## Como verificar
Execute dois casos raiz que leem o mesmo campo e um descendente de cada, confirmando valores distintos entre raízes e compartilhados dentro da raiz.

## Conexões
- [[kotest-concorrencia-de-testes-e-estado-mutavel]] — Veja também: Kotest 6.2: habilitar concorrência só depois de definir segurança de estado.

## Fontes
- [Kotest 6.2 — Isolation Modes](https://kotest.io/docs/framework/isolation-mode.html) — instâncias de Spec, SingleInstance, InstancePerRoot e modos depreciados; consultado em 2026-10-02.
- [Kotest 6.2 — Project Level Config](https://kotest.io/docs/framework/project-config.html) — configuração de engine no nível do projeto e precedência; consultado em 2026-10-02.
