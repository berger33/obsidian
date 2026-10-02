---
id: software.testes.pytest-fixtures-escopo.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://docs.pytest.org/en/stable/how-to/fixtures.html", "https://docs.pytest.org/en/stable/reference/fixtures.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [pytest fixtures, Fixture scope pytest, Setup and teardown pytest]
lote: software-testes-2000-0001
---

# Fixtures do pytest: ciclo de vida e escopos

## Em uma frase
Fixtures do pytest preparam recursos para testes e podem compartilhá-los segundo um escopo explícito, do caso individual até a sessão inteira.

## Por que importa
Fixtures tornam setup e dependências visíveis na assinatura do teste, mas escopos amplos também prolongam o ciclo de vida e podem compartilhar estado entre casos. A escolha afeta custo, isolamento, paralelismo e limpeza de recursos como conexão, diretório temporário ou servidor local. Um fixture reutilizável não deve fazer o teste depender silenciosamente de uma ordem específica.

## Como funciona
`@pytest.fixture` declara uma função de fixture. Por padrão, `scope="function"` cria o recurso para cada teste que o solicita e o descarta ao final do teste. `class`, `module`, `package` e `session` ampliam o período de compartilhamento. Dependências entre fixtures e seus escopos também influenciam a ordem de inicialização. Uma fixture que usa `yield` pode executar a limpeza depois do ponto de yield; essa finalização acontece após o teste consumidor terminar.

## Exemplo
Uma fixture de banco em memória com escopo de função oferece estado novo para cada caso e reduz interferência. Se criar um recurso for caro, um escopo de módulo pode ser considerado, mas os testes precisam resetar dados mutáveis entre execuções. Um servidor local pode ser iniciado por uma fixture e encerrado na etapa de teardown.

## Limites e trade-offs
Escopo `session` não torna automaticamente um recurso seguro para concorrência ou imutabilidade. Fixtures `autouse` podem introduzir setup invisível e aumentar acoplamento. Scope controla disponibilidade e duração, não hermeticidade, correção do serviço nem isolamento de efeitos externos. Confirme o comportamento de plugins e versão do pytest usados no projeto.

## Como verificar
Execute os casos em ordem diferente e em paralelo quando suportado; confirme que setup produz estado conhecido e teardown remove recursos mesmo após falha. Inspecione dependências de fixtures, escopos compartilhados e fixtures `autouse`. Reduza o escopo quando compartilhamento não for necessário e meça setup antes de ampliá-lo por desempenho.

## Conexões
- [[testes-hermeticos-dependencias]] — fixtures ajudam a prover dependências locais e declaradas.
- [[testes-flaky-determinismo]] — estado compartilhado ou limpeza incompleta pode produzir flakiness.
- [[test-doubles-fakes-stubs-spies-mocks]] — fixtures podem compor doubles para o sistema sob teste.

## Fontes
- [pytest — How to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) — setup, dependências e finalização de recursos; acesso em 2026-10-01.
- [pytest — Fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html) — escopos, disponibilidade e ordem de instância; acesso em 2026-10-01.
