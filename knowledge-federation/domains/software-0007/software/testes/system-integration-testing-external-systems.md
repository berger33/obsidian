---
id: software.testes.system-integration.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-05.md"
revisor: ""
fontes: ["https://astqb.org/2-2-test-levels-and-test-types/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [System integration testing, SIT, Teste de integração de sistemas]
lote: software-testes-2000-0001
---

# Integração do sistema com serviços externos

## Em uma frase
System integration testing foca nas interfaces entre o sistema sob teste e outros sistemas ou serviços externos.

## Por que importa
Um sistema pode passar seus testes internos e falhar ao trocar mensagens, autenticar, negociar versões ou tratar indisponibilidade de um fornecedor. Testar a fronteira entre sistemas evidencia problemas de protocolo, configuração e comportamento distribuído que testes internos não exercitam.

## Como funciona
O CTFL descreve SIT como teste das interfaces do sistema sob teste com outros sistemas e serviços externos. Requer ambiente adequado, preferencialmente semelhante ao operacional; contudo, acesso a sistemas externos pode ser limitado, caro ou arriscado. O nível deve definir quais dependências são reais, virtualizadas ou simuladas e quais propriedades cada forma consegue verificar.

## Exemplo
Uma plataforma de comércio conecta-se a uma adquirente em sandbox. Testes validam autenticação, formato de requisição, códigos de resposta, repetição segura e timeout. A sandbox pode não reproduzir todos os limites ou falhas de produção, então registre diferenças e complemente com testes de contrato ou simulação controlada.

## Limites e trade-offs
A equipe pode controlar apenas um lado da interface; disponibilidade e dados do parceiro afetam resultados. Ambiente “parecido” não é prova de equivalência completa. Testes em produção, se usados, exigem controles de segurança e blast radius.

## Como verificar
Mapeie sistemas/interfaces, versões, credenciais não sensíveis, dados e modos de falha. Valide comportamento nominal e erros relevantes, preserve logs sem segredos e declare quais partes foram simuladas. Separe defeitos do sistema, do fornecedor e de configuração.

## Conexões
- [[component-integration-testing-interfaces]] — trata integração dentro do produto.
- [[testes-hermeticos-dependencias]] — controla dependências em testes repetíveis.
- [[test-environment-configuration-management]] — registra ambiente e versões usados.

## Fontes
- [ASTQB — ISTQB CTFL §2.2: Test Levels and Test Types](https://astqb.org/2-2-test-levels-and-test-types/) — níveis e atributos de distinção; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — seção 2.2.1, interfaces externas e ambiente SIT; acesso em 2026-10-01.
