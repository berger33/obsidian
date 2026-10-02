---
id: software.testes.tranche13.000743
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://cmake.org/cmake/help/latest/command/add_test.html", "https://cmake.org/cmake/help/latest/manual/ctest.1.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# CTest: usar WILL_FAIL só para processo com erro esperado

## Em uma frase
Por padrão, código de saída zero aprova teste e código diferente de zero o reprova; `WILL_FAIL` inverte essa lógica para casos que esperam retorno de falha.

## Por que importa
Registrar erro como sucesso esperado permite verificar CLI sem ocultar que contrato do programa é rejeitar aquela entrada.

## Como funciona
Use WILL_FAIL no teste negativo nomeado, combine com checagem de mensagem quando precisa verificar motivo e não interprete crash de sistema como retorno de erro comum.

## Exemplo
Um comando de validação recebe configuração inválida e deve sair com status não zero; segundo teste confirma texto da explicação produzida.

## Limites e trade-offs
Segfault e falhas de sistema continuam falhando mesmo com WILL_FAIL; inverter código sem checar output pode aceitar causa errada.

## Como verificar
Force uma saída não zero controlada e um crash em executáveis descartáveis e compare resultados apresentados por CTest.

## Conexões
- [[ctest-working-directory-contract]] — Veja também: CTest: fixar working directory para dados relativos.
- [[ctest-timeout-failure-diagnostic]] — Veja também: CTest: limitar duração com propriedade TIMEOUT.

## Fontes
- [CMake — add_test](https://cmake.org/cmake/help/latest/command/add_test.html) — test registration, command, working directory and target handling; consultado em 2026-10-02.
- [CMake — ctest(1)](https://cmake.org/cmake/help/latest/manual/ctest.1.html) — selection, parallel scheduling, presets, repeat and output; consultado em 2026-10-02.
