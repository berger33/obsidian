---
id: software.seguranca.tranche12.001130
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/mitre/caldera/master/README.md", "https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Extensibilidade do Caldera: Criando **Plugins Customizados (`mitre/skeleton`)**, Novos **Parsers de Fatos** e **Planners** Sob Medida

## Em uma frase
Quando a equipe de Engenharia de Detecção ou Red Team da sua empresa precisa emular fluxos específicos do seu negócio (por exemplo, interagir com uma API interna de pagamentos, extrair tokens de um cofre proprietário com um parser customizado ou implementar uma lógica de decisão em árvore que não existe nos planners padrão), você pode criar seu próprio **Plugin do Caldera**!

## Por que importa
A MITRE disponibiliza o gerador oficial **`skeleton` (`mitre/skeleton`)**, que cria a estrutura padrão de um plugin em `plugins/<meu_plugin>/` contendo `hook.py` (ponto de entrada assíncrono chamado na inicialização do servidor Caldera), diretórios `data/abilities/`, `data/adversaries/`, `data/payloads/` e módulos Python para novos **Parsers** e **Planners**!

## Como funciona
Um **Parser customizado** em Python herda de `BaseParser`, recebe o `blob` de texto retornado pelo agente após a execução de um comando e emite objetos `Relationship(source, edge, target)` que populam automaticamente o grafo de fatos da operação!

## Exemplo
```python
# Exemplo conciso de hook.py de um plugin customizado do MITRE Caldera carregando um diretorio proprio de Abilities e Adversaries
name = "CorpPurple"
description = "Plugin interno de TTPs e Parsers customizados do Purple Team corporativo"
address = None

async def enable(services):
    data_svc = services.get("data_svc")
    await data_svc.load_data("plugins/corppurple/data")
```

## Limites e trade-offs
Ao adicionar um novo plugin ao Caldera v5 ou alterar componentes visuais, execute `python3 server.py --build` uma vez para que o empacotador VueJS (**Magma**) compile e integre a interface do novo plugin no diretório `dist/`.

## Como verificar
Mantenha seus plugins internos em um repositório Git privado separado e monte-o dentro de `plugins/` durante o deploy automatizado do seu laboratório Purple Team.

## Conexões
- [[caldera-hardening-seguranca-implantacao-ssl-local-yml-autenticacao]] — Veja também: Hardening e Segurança Operacional de uma Implantação do **MITRE Caldera**: `conf/local.yml`, Plugin **`ssl`**, **`saml`** e Isolamento de Rede.
- [[caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins]] — Referência cruzada direta com caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins.
- [[caldera-abilities-adversary-profiles-planners-facts-parsers]] — Referência cruzada direta com caldera-abilities-adversary-profiles-planners-facts-parsers.
- [[atomicredteam-desenvolvimento-novos-atomics-validacao-ci-pre-commit]] — Referência cruzada direta com atomicredteam-desenvolvimento-novos-atomics-validacao-ci-pre-commit.

## Fontes
- [MITRE Caldera Official GitHub — Automated Adversary Emulation, Red Team & Incident Response Platform](https://raw.githubusercontent.com/mitre/caldera/master/README.md) — repositório oficial do MITRE Caldera v5 cobrindo o Core C2 Server, interface VueJS Magma e ecossistema de plugins (`sandcat`, `stockpile`, `atomic`, `emu`, `debrief`, `response`); consultado em 2026-10-03.
- [MITRE Caldera Official Documentation — Learning the Terminology (`Agents`, `Abilities`, `Adversaries`, `Operations`, `Planners`, `Facts`, `Parsers`)](https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html) — documentação oficial ReadTheDocs detalhando a arquitetura de planejamento orientado a fatos e agentes do Caldera; consultado em 2026-10-03.
