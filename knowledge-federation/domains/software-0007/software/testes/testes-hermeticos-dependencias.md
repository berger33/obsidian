---
id: software.testes.testes-hermeticos.000001
tipo: conceito
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
fontes: ["https://bazel.build/reference/test-encyclopedia", "https://abseil.io/resources/swe-book/html/ch23.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Hermetic test, Hermetic testing, Teste hermético]
lote: software-testes-2000-0001
---

# Testes herméticos e dependências declaradas

## Em uma frase
Um teste hermético depende apenas dos insumos e recursos que declara, reduzindo influência de serviços, estado ou ambiente externos não controlados.

## Por que importa
Um teste que depende da rede pública, de um banco compartilhado ou de arquivos deixados por outra execução pode passar em uma máquina e falhar em outra. Isso dificulta reproduzir regressões, atribuir a causa a uma mudança e executar testes em paralelo. Hermeticidade é uma propriedade do ambiente e das dependências, não uma prova de que a asserção do teste está correta.

## Como funciona
A Test Encyclopedia do Bazel descreve testes como herméticos quando acessam somente recursos com dependência declarada, e define o resultado esperado em função de arquivos-fonte, produtos da build e recursos garantidos pelo runner. O livro Software Engineering at Google descreve ambientes herméticos como autocontidos, sem dependências externas como backends de produção; eles tendem a melhorar determinismo e isolamento. Uma implementação pode usar serviços locais, dados de teste e doubles bem definidos, ou iniciar um servidor real no próprio ambiente de teste.

## Exemplo
Um teste de integração que precisa de armazenamento pode iniciar uma instância efêmera com versão fixa e carga de dados conhecida, em vez de usar o banco de desenvolvimento de uma pessoa. Uma dependência remota que não é o objeto do teste pode ser substituída por um fake. O sistema de build deve declarar os arquivos e executáveis necessários, sem buscar recursos arbitrários durante a execução.

## Limites e trade-offs
Ambientes herméticos têm custo de criação e podem não reproduzir exatamente produção. Fakes e servidores simulados precisam continuar alinhados aos contratos reais; testes herméticos não eliminam a necessidade de testes de contrato, integração externa ou operação em staging. Tempo do sistema, aleatoriedade e concorrência ainda podem causar não determinismo se não forem controlados.

## Como verificar
Execute o teste sem acesso à rede externa e com diretório de trabalho limpo. Repita em outra máquina/worker e em paralelo; o resultado deve depender somente das entradas declaradas. Inspecione dependências implícitas de relógio, variáveis de ambiente, ordem de testes, serviço compartilhado e arquivos locais; registre explicitamente aquilo que o teste precisa.

## Conexões
- [[test-doubles-fakes-stubs-spies-mocks]] — doubles são uma técnica para substituir algumas dependências.
- [[testes-flaky-determinismo]] — dependências externas e estado compartilhado são fontes de resultados instáveis.
- [[fixtures-pytest-ciclo-vida-escopos]] — fixtures podem montar e limpar recursos do teste.

## Fontes
- [Bazel — Test Encyclopedia](https://bazel.build/reference/test-encyclopedia) — hermeticidade, dependências e ambiente de execução de testes Bazel; acesso em 2026-10-01.
- [Software Engineering at Google — Continuous Integration, seção Hermetic Testing](https://abseil.io/resources/swe-book/html/ch23.html) — determinismo, isolamento e custos de ambientes herméticos; acesso em 2026-10-01.
