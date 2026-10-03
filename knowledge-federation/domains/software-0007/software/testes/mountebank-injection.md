---
id: software.testes.tranche19.001283
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://www.mbtest.org/docs/api/injection", "https://www.mbtest.org/docs/api/overview"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mountebank: calcular respostas com injeção

## Em uma frase
A injeção executa função em JavaScript para decidir o predicado ou montar a resposta, com acesso à requisição recebida.

## Por que importa
A lógica programática cobre handshakes e respostas dependentes de estado que a configuração declarativa não expressa bem.

## Como funciona
Restrinja a injeção a casos necessários, mantenha as funções pequenas e habilite a opção correspondente ao iniciar o serviço.

## Exemplo
Uma função pode validar um token simples e responder com o cabeçalho esperado apenas quando a verificação passa.

## Limites e trade-offs
Injeção habilitada sem controle executa código arbitrário, e lógica extensa dentro da função vira software sem teste próprio.

## Como verificar
Desligue a opção de injeção e confirme que o impostor que depende dela passa a falhar ao subir.

## Conexões
- [[mountebank-behaviors]] — Veja também: Mountebank: ajustar respostas com comportamentos.
- [[mountebank-recorded-requests]] — Veja também: Mountebank: inspecionar requisições recebidas.

## Fontes
- [Mountebank — Injection](https://www.mbtest.org/docs/api/injection) — predicados e respostas calculados por função JavaScript; consultado em 2026-10-03.
- [Mountebank — API overview](https://www.mbtest.org/docs/api/overview) — interface administrativa, criação de impostores e remoção; consultado em 2026-10-03.
