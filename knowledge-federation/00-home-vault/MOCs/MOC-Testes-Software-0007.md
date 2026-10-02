# MOC — Testes de Software (lote 0007)

Índice das 149 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 149 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 140 aprovadas por IA, sem converter estas últimas em aprovações humanas. Este mapa é navegação, não validação factual.

## Fundamentos, processo e testware
- [[test-objectives-context]] — selecionar objetivos conforme work product, riscos e contexto.
- [[testing-principles-contextual]] — usar os sete princípios como orientação contextual.
- [[error-defect-failure-root-cause]] — distinguir erro, defeito, falha e causa raiz.
- [[testing-vs-debugging]] — separar evidência de teste da investigação/correção.
- [[fundamental-test-activities]] — planejar, analisar, desenhar, implementar, executar e concluir.
- [[test-process-context-tailoring]] — adaptar atividades à situação, sem adotar receita única.
- [[testing-roles-management-and-testing]] — distinguir responsabilidades de gestão e função técnica.
- [[testware-artifacts]] — organizar os produtos de trabalho gerados pelas atividades.

## Teste estático, feedback e revisões
- [[static-testing-work-products]] — revisar work products e aplicar análise estática sem execução.
- [[static-vs-dynamic-testing]] — combinar evidências de abordagens complementares.
- [[early-frequent-stakeholder-feedback]] — obter feedback de stakeholders ao longo do SDLC.
- [[review-process-activities]] — estruturar planejamento, leitura, comunicação e tratamento de findings.
- [[review-types-formality-purpose]] — selecionar tipo de revisão conforme objetivo e risco.
- [[review-success-factors]] — preparar participantes e medir sucesso sem avaliar indivíduos.

## Níveis de teste
- [[test-levels-overview]] — comparar os cinco níveis do CTFL e seus objetivos.
- [[component-testing-isolation]] — avaliar componentes isolados.
- [[component-integration-testing-interfaces]] — examinar interações entre componentes.
- [[system-testing-requirements]] — verificar comportamento do sistema integrado.
- [[system-integration-testing-external-systems]] — testar interfaces com sistemas/serviços externos.
- [[acceptance-testing-validation]] — validar necessidades e readiness para uso/implantação.

## SDLC, manutenção e tipos de teste
- [[sdlc-impact-on-testing]] — relaciona o ciclo de vida ao escopo, timing e abordagem.
- [[testing-sequential-and-iterative-sdlc]] — compara cadência e sobreposição das atividades.
- [[good-testing-practices-across-sdlc]] — práticas de teste úteis em vários modelos.
- [[test-first-approaches-tdd-atdd-bdd]] — situa TDD, ATDD e BDD.
- [[test-driven-development]] — orienta código por testes escritos antes.
- [[acceptance-test-driven-development]] — deriva casos de critérios de aceitação.
- [[behavior-driven-development]] — comunica comportamento com exemplos.
- [[devops-testing-continuous-feedback]] — aproxima desenvolvimento, teste e operação.
- [[shift-left-testing]] — antecipa verificação sem retirar testes posteriores.
- [[testing-retrospectives-process-improvement]] — transforma experiência em melhorias acompanhadas.
- [[maintenance-testing-change-scope]] — considera risco e tamanho da mudança.
- [[maintenance-testing-triggers]] — cobre modificações, migrações e aposentadoria.
- [[testing-migrations-and-platform-upgrades]] — verifica ambiente e conversão de dados.
- [[retirement-testing-data-archival]] — valida arquivamento e recuperação.
- [[independence-of-testing-levels]] — compara níveis de independência.
- [[whole-team-approach-quality]] — compartilha responsabilidade quando apropriado.
- [[essential-skills-for-testers]] — mapeia competências para o trabalho de teste.
- [[functional-testing-quality-characteristics]] — verifica o que o sistema faz.
- [[nonfunctional-testing-quality-attributes]] — avalia como o sistema se comporta.
- [[confirmation-testing-after-fix]] — confirma correções.
- [[regression-testing-change-effects]] — identifica efeitos colaterais de mudanças.
- [[black-box-testing-specification-based]] — deriva testes da especificação.
- [[white-box-testing-structure-and-limits]] — usa a estrutura interna como base.
- [[experience-based-testing-techniques]] — organiza técnicas baseadas em experiência.
- [[error-guessing-experience]] — formula hipóteses a partir do histórico.
- [[checklist-based-testing]] — mantém condições focadas em uma lista.
- [[collaboration-based-test-approach]] — usa conversa para evitar defeitos.
- [[user-story-three-cs]] — organiza Card, Conversation e Confirmation.
- [[acceptance-criteria-as-test-conditions]] — trata critérios como condições testáveis.

## Papéis de revisão e suporte de ferramentas
- [[review-roles-responsibilities]] — distribui tarefas entre papéis da revisão.
- [[review-moderator-facilitator]] — facilita reuniões construtivas.
- [[review-scribe-recorder]] — registra findings e decisões.
- [[review-reviewer-role]] — examina work products e descreve anomalias.
- [[review-author-feedback-correction]] — cria e corrige o material revisado.
- [[review-leader-responsibility]] — responde pela organização geral.
- [[review-manager-resources]] — define prioridade e disponibiliza recursos.
- [[review-role-allocation-context]] — adapta a alocação ao risco e à formalidade.
- [[test-tool-categories]] — organiza categorias por atividade apoiada.
- [[test-tools-beyond-automation]] — inclui gestão, revisão e colaboração.
- [[test-tool-introduction-and-risk]] — planeja adoção, treinamento e mitigação.

## Isolamento, confiabilidade e regressão
- [[test-doubles-fakes-stubs-spies-mocks]] — escolher doubles conforme o papel e a forma de verificação.
- [[testes-hermeticos-dependencias]] — controlar e declarar dependências do ambiente.
- [[testes-flaky-determinismo]] — diagnosticar resultados inconsistentes.
- [[fixtures-pytest-ciclo-vida-escopos]] — controlar preparação, escopo e limpeza no pytest.
- [[snapshot-testing-jest-revisao]] — detectar mudanças de saída com snapshots revisados.
- [[regression-test-prioritization-risco-impacto]] — ordenar testes de regressão considerando impacto e risco.

## Seleção de dados e combinações
- [[particionamento-equivalencia-valores-fronteira]] — selecionar representantes de classes e exercitar limites.
- [[decision-table-testing-regras-condicionais]] — cobrir regras definidas por combinações de condições.
- [[combinatorial-testing-pairwise-t-way]] — cobrir interações t-way de parâmetros.

## Geração de casos, propriedades e sequências
- [[property-based-testing-hypothesis]] — expressar propriedades sobre entradas geradas.
- [[shrinking-contraexemplos-hypothesis]] — simplificar entradas que reproduzem uma falha.
- [[testes-stateful-model-based-hypothesis]] — gerar sequências de operações sobre sistemas com estado.
- [[state-transition-testing-coverage]] — derivar sequências e critérios de cobertura de modelos de estado.
- [[fuzzing-coverage-guided-libfuzzer]] — explorar caminhos com fuzzing guiado por cobertura.
- [[metamorphic-testing-oracle-relations]] — verificar relações entre execuções sem exigir oracle completo.
- [[differential-testing-comparacao-implementacoes]] — investigar divergências entre implementações equivalentes.
- [[test-oracles-resultados-esperados]] — escolher critérios para avaliar resultados de teste.

## Exploração e gestão de risco
- [[risk-based-testing-priorizacao-risco]] — concentrar esforço nos riscos de maior probabilidade e impacto.
- [[exploratory-testing-aprendizado-design-execucao]] — aprender, projetar e executar testes de forma integrada.
- [[session-based-testing-charters-debriefs]] — estruturar a exploração com missão, relato e debrief.

## Cobertura e eficácia das verificações
- [[cobertura-branches-statement-interpretacao]] — distinguir cobertura de statements e branches.
- [[mcdc-coverage-condicoes-independentes]] — verificar o efeito independente de condições lógicas.
- [[mutation-testing-eficacia-testes]] — verificar se a suíte detecta alterações de comportamento.
- [[piramide-testes-estrategia-contexto]] — distribuir testes conforme risco, custo e arquitetura.

## Acessibilidade, desempenho e resiliência
- [[teste-acessibilidade-automatizada-revisao-humana]] — combinar scanner com avaliação manual de tarefas acessíveis.
- [[performance-testing-modelagem-carga]] — modelar carga e critérios de desempenho.
- [[chaos-experiments-steady-state-blast-radius]] — testar resiliência com hipóteses e impacto controlado.

## Contratos de API e dados
- [[schema-based-api-testing-schemathesis-openapi]] — gerar casos de API a partir de um schema.
- [[test-data-privacidade-sinteticos]] — reduzir exposição e avaliar utilidade de dados de teste.

## Planejamento, controle e governança do teste
- [[test-planning-objetivos-escopo-comunicacao]] — alinhar objetivos, recursos, cronograma e comunicação.
- [[test-entry-exit-criteria]] — definir condições para iniciar e concluir atividades.
- [[test-effort-estimation-techniques]] — estimar esforço com métodos baseados em dados ou especialistas.
- [[test-case-prioritization-dependencies]] — ordenar casos considerando risco, cobertura e dependências.
- [[test-progress-metrics-relatorios-conclusao]] — monitorar resultados e comunicar progresso/encerramento.
- [[test-environment-configuration-management]] — manter versões e contexto reproduzíveis para testware.
- [[requirements-test-traceability]] — ligar base de teste, casos, resultados e defeitos.
- [[defect-report-reproducibility-severity-priority]] — registrar anomalias que possam ser reproduzidas e triadas.
- [[test-automation-investment-maintenance-risks]] — avaliar investimento, ROI e manutenção de automação.
- [[ci-feedback-testes-regressao]] — usar CI para fornecer feedback frequente e controlado.

## Desempenho: perfis de carga, percentis e testes de capacidade
- [[testes-latencia-percentis-thresholds]] — Defina limites de desempenho sobre percentis de latência, taxa de erros e objetivos de serviço, em vez de depender apenas da média.
- [[testes-correcao-funcional-sob-carga]] — Verifique respostas e invariantes funcionais enquanto o sistema atende carga, sem confundir sucesso HTTP isolado com correção do fluxo.
- [[testes-modelagem-carga-vus-taxa-chegada]] — Selecione um modelo aberto ou fechado de geração de carga de acordo com a pergunta que o teste pretende responder.
- [[testes-smoke-carga-minima-api]] — Use uma execução curta e de baixa carga para confirmar que o script, os endpoints principais e o ambiente respondem antes de testes maiores.
- [[testes-carga-media-perfil-trafego]] — Avalie o serviço com um perfil que represente tráfego típico, mix de operações e duração operacional relevante para a decisão.
- [[testes-stress-limite-capacidade]] — Aumente a carga de forma controlada acima do padrão esperado para observar degradação, ponto de saturação e recuperação.
- [[testes-spike-picos-abruptos]] — Simule uma subida rápida de carga para examinar se filas, autoscaling e dependências suportam mudanças abruptas e como o serviço se recupera.
- [[testes-soak-degradacao-temporal]] — Mantenha uma carga representativa por período prolongado para procurar degradação lenta que testes curtos não revelam.
- [[testes-breakpoint-rampa-carga]] — Aumente gradualmente a taxa ou concorrência para localizar a faixa em que o sistema deixa de cumprir critérios operacionais.
- [[testes-canary-validacao-telemetria]] — Use uma parcela controlada de tráfego real para observar se uma versão nova preserva sinais de saúde antes de ampliar o rollout.

## Acessibilidade: critérios WCAG e regressão multimodal
- [[teste-acessibilidade-navegacao-teclado]] — Verifique se ações e conteúdo operáveis podem ser alcançados e acionados sem mouse, respeitando o comportamento esperado de cada controle.
- [[teste-acessibilidade-foco-visivel-ordem]] — Examine se o foco de teclado permanece visível e percorre uma sequência que preserva significado e operabilidade.
- [[teste-acessibilidade-rotulos-erros-formulario]] — Confirme que controles têm rótulos e instruções associados e que erros identificam o campo, o problema e a forma de correção.
- [[teste-acessibilidade-nome-papel-valor]] — Valide se controles nativos e customizados expõem nome acessível, papel e estado coerentes com a função e com a interação atual.
- [[teste-acessibilidade-contraste]] — Meça contraste nas cores efetivamente renderizadas em cada estado relevante e confronte os resultados com o critério WCAG aplicável.
- [[teste-acessibilidade-reflow-zoom]] — Avalie se conteúdo e funcionalidade permanecem disponíveis quando o viewport é estreito ou o usuário amplia o conteúdo, sem exigir rolagem bidimensional indevida.
- [[teste-acessibilidade-wcag-target-size]] — Meça os alvos de entrada por ponteiro e avalie o requisito mínimo de tamanho ou as exceções de espaçamento definidas no critério.
- [[teste-acessibilidade-autenticacao-acessivel]] — Verifique se o processo de autenticação evita exigir uma função cognitiva sem alternativa ou apoio permitido pelo critério de acessibilidade aplicável.
- [[teste-acessibilidade-status-dinamico]] — Confirme que mensagens de sucesso, erro, progresso ou resultado de ação são programaticamente determináveis sem depender de uma mudança de foco.
- [[teste-acessibilidade-regressao-multimodal]] — Combine verificações automatizadas repetíveis com percursos manuais de teclado, zoom e tecnologia assistiva para detectar regressões de acesso.

## Segurança: autorização, sessão, entrada, headers e logs
- [[testes-autorizacao-horizontal-objetos]] — Verifique se uma conta autenticada consegue ler ou alterar somente os objetos pertencentes ao seu próprio escopo.
- [[testes-autorizacao-vertical-privilegios]] — Avalie se usuários de menor privilégio são impedidos de executar funções reservadas a papéis superiores, inclusive por chamadas diretas.
- [[testes-sessao-idle-timeout-replay]] — Verifique se a sessão expira por inatividade conforme a política e se um identificador invalidado não volta a autorizar requisições.
- [[testes-session-fixation-regeneracao-id]] — Confirme que uma sessão pré-autenticação não conserva o mesmo identificador depois que a identidade ou o privilégio da conta muda.
- [[testes-csrf-origem-token-cookie]] — Examine se uma operação que altera estado rejeita solicitações cross-site não autorizadas e se proteções são avaliadas no contexto real dos cookies.
- [[testes-validacao-input-reflected-xss]] — Siga entradas controladas até o contexto de saída e verifique se texto não confiável é exibido como dado, sem execução de conteúdo ativo.
- [[testes-ssrf-destino-url-egress]] — Avalie se uma funcionalidade que busca URLs limita destinos e protocolos a uma política explícita, sem alcançar recursos internos não autorizados.
- [[testes-autenticacao-rate-limit-enumeracao]] — Verifique que tentativas automatizadas são limitadas sem expor a existência de contas nem permitir que um teste cause bloqueio de usuários reais.
- [[testes-security-headers-browser]] — Inspecione cabeçalhos emitidos em respostas relevantes e valide se sua política corresponde à arquitetura e ao comportamento esperado do navegador.
- [[testes-logs-redaction-injection]] — Verifique que eventos necessários são registrados, dados secretos são excluídos ou mascarados e entradas não confiáveis não forjam registros.

## Confiabilidade, recuperação e rollout
- [[testes-degradacao-graciosa-invariantes]] — Introduza indisponibilidade ou lentidão de uma dependência e verifique se o serviço preserva operações essenciais ou comunica uma falha controlada.
- [[testes-load-shedding-limites-sobrecarga]] — Examine se, sob sobrecarga, o sistema limita trabalho e rejeita solicitações de forma controlada antes de comprometer todos os recursos.
- [[testes-retry-backoff-jitter-cascata]] — Valide que novas tentativas são limitadas, espaçadas e seguras para a operação, evitando multiplicar a carga quando uma dependência falha.
- [[testes-falha-dependencia-timeout-circuit-breaker]] — Simule timeout e falha de serviço dependente para confirmar orçamento de espera, abertura do circuit breaker e recuperação controlada.
- [[testes-restore-backup-integridade]] — Restaure um backup em ambiente isolado e confirme que dados e serviço podem ser recuperados, não apenas que o arquivo existe.
- [[testes-recuperacao-rto-rpo]] — Meça em exercício controlado se a recuperação atende objetivos declarados de tempo e perda máxima de dados, incluindo dependências necessárias.
- [[testes-canary-comparacao-baseline]] — Compare a versão canário e a versão estável por métricas e resultados sob condições suficientemente semelhantes antes de promover a mudança.
- [[testes-kubernetes-rolling-update-disponibilidade]] — Exercite uma atualização progressiva e confirme estado do Deployment, prontidão dos Pods e continuidade das operações esperadas.
- [[testes-rollback-versao-estado]] — Prove que uma implantação problemática pode ser revertida e que a versão anterior opera com o estado produzido durante a atualização.
- [[testes-probes-startup-liveness-readiness]] — Teste cada probe segundo seu propósito: permitir inicialização, reiniciar processo travado ou retirar temporariamente tráfego de instância não pronta.

## HTTP, contratos e integridade de dados
- [[testes-http-content-negotiation-vary]] — Verifique se o servidor escolhe uma representação compatível com Accept e outras preferências documentadas e se caches distinguem variantes quando necessário.
- [[testes-semantica-metodos-http-idempotencia]] — Verifique que métodos aceitos produzem os efeitos definidos pelo contrato HTTP, incluindo segurança, idempotência e resposta adequada a métodos não permitidos.
- [[testes-api-problem-details-rfc9457]] — Valide que erros publicados com Problem Details respeitam mídia, semântica HTTP e estrutura prevista no contrato, sem expor detalhes internos.
- [[testes-http-conditional-requests-etag]] — Exercite validators e precondições HTTP para detectar cache condicional e conflitos de atualização sem sobrescrever silenciosamente estado concorrente.
- [[testes-pagination-cursor-invariantes]] — Verifique que a navegação por cursor mantém ordem e cobertura previstas no contrato diante de limites, filtros e alterações concorrentes controladas.
- [[testes-api-rate-limit-429-retry-after]] — Valide a resposta à quota excedida e se clientes e caches respeitam o contrato de limitação de taxa sem retentar de forma agressiva.
- [[testes-contract-testing-compatibilidade-api]] — Combine validação de schema com interações que representam necessidades reais de consumidores para detectar incompatibilidades antes do deploy.
- [[testes-consumer-idempotency-duplicates]] — Entregue a mesma mensagem mais de uma vez e confirme que consumidor produz no máximo o efeito de negócio definido para aquele identificador.
- [[testes-consistencia-eventual-convergencia]] — Verifique se leituras eventualmente consistentes convergem dentro do comportamento e prazo operacional declarados, sem exigir visibilidade imediata não prometida.
- [[testes-database-integrity-reconciliation]] — Verifique invariantes de dados tanto no limite transacional do banco quanto em reconciliações independentes entre fontes ou projeções.

## Estado editorial
O gate automatizado foi aprovado por 149/149 notas e as 149 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 140 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (149 notas substantivas; 1.851 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-testes-2000-0001.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-testes-2000-0001.md), os relatórios factuais por IA das [tranches 2–3](../../exports/reports/ai-review-software-testes-2000-0001.md), da [tranche 4](../../exports/reports/ai-review-software-testes-2000-0001-tranche-04.md), da [tranche 5](../../exports/reports/ai-review-software-testes-2000-0001-tranche-05.md), da [tranche 6](../../exports/reports/ai-review-software-testes-2000-0001-tranche-06.md) e da [tranche 7](../../exports/reports/ai-review-software-testes-2000-0001-tranche-07.md), e o [registro de revisão humana e IA](../../exports/reports/human-review-queue.md).
