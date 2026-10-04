---
id: software.testes.tranche19.001312
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
fontes: ["https://github.com/bridgecrewio/checkov/tree/master/checkov/secrets", "https://github.com/bridgecrewio/checkov"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Checkov: detectar segredos em arquivos de infraestrutura

## Em uma frase
O verificador de segredos procura credenciais e chaves por padrões, palavras-chave e análise de entropia em arquivos e blocos de configuração.

## Por que importa
Segredos embutidos em configuração de infraestrutura permanecem no histórico e exigem rotação, não apenas remoção da linha atual.

## Como funciona
Ative o verificador, trate cada achado como incidente, rotacione a credencial e substitua o valor por referência a cofre.

## Exemplo
Uma chave de acesso em bloco de dados de inicialização precisa ser revogada e passar a vir de parâmetro protegido.

## Limites e trade-offs
A detecção pode marcar cadeias de alta entropia sem risco, e a ausência de achado não garante que todos os segredos foram removidos.

## Como verificar
Insira uma credencial fictícia em arquivo de teste e confirme que ela aparece no relatório com o caminho correspondente.

## Conexões
- [[checkov-baseline]] — Veja também: Checkov: separar passivo antigo de achados novos.
- [[checkov-custom-policies]] — Veja também: Checkov: escrever políticas próprias.

## Fontes
- [Checkov — Verificações de segredos](https://github.com/bridgecrewio/checkov/tree/master/checkov/secrets) — detecção de credenciais por padrões, palavras-chave e entropia; consultado em 2026-10-03.
- [Checkov — repositório oficial](https://github.com/bridgecrewio/checkov) — código-fonte, verificações e documentação do projeto; consultado em 2026-10-03.
