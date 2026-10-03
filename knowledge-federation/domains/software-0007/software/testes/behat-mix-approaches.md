---
id: software.testes.tranche24.001826
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://docs.behat.org/en/latest/", "https://raw.githubusercontent.com/Behat/Behat/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Misture tecnologias: navegador, HTTP, shell, banco e PHP direto

## Em uma frase
Ainda na seção de cobertura total, a doc oficial explicita o cardápio: "This allows you to 'mix and match' different testing approaches and technologies. Browser automation; HTTP API calls; running shell commands; communicating directly with your database, filesystem or PHP code: anything is possible."

## Por que importa
A mistura por passo resolve o dilema clássico de testes de sistema: cenários não precisam pagar o custo do navegador quando o contrato HTTP basta, nem engolir a fragilidade do browser quando a UI é o que se prova — a escolha vira tática local por cenário, não religião global do repositório.

## Como funciona
Num cenário de checkout, prove o recibo no banco (passo de consulta direta), o e-mail (step de filesystem/inbox) e a página de confirmação (passo de browser automation) — todos no mesmo .feature, cada um na camada que documenta melhor.

## Exemplo
A doc lista as cinco famílias explicitamente — navegador, HTTP, shell, banco/arquivos e código PHP — o que autoriza a dizer que steps de subprocesso são de primeira classe no modelo do Behat.

## Limites e trade-offs
"Anything is possible" descreve a arquitetura de steps; cada tecnologia na prática depende de extensões e integrações — a nota cita as famílias nomeadas, não uma biblioteca por família.

## Como verificar
A frase do mix and match está na seção "Cover your whole application" da doc oficial.

## Conexões
- [[behat-full-application-scope]] — Veja também: Cobrindo a aplicação inteira, não camadas.
- [[behat-profiles-tags-suites]] — Veja também: Profiles, tags e suites: o mesmo feature, jeitos diferentes.

## Fontes
- [Behat — documentação oficial (en/latest)](https://docs.behat.org/en/latest/) — Página inicial da documentação oficial do Behat com exemplo Gherkin, cobertura de aplicação inteira, profiles/tags/suites, componentes Symfony e extensões.; consultado em 2026-10-03.
- [Behat — README oficial](https://raw.githubusercontent.com/Behat/Behat/master/README.md) — README oficial do Behat com instalação via Composer, versão de desenvolvimento, política SemVer/BC, mantenedores e canais de apoio.; consultado em 2026-10-03.
